"""Tire des treebanks les fréquences et les exemples de chaque fiche, et écrit les fragments
Markdown que les fiches incluent (generes/<fiche>-frequences.<langue>.md, generes/<fiche>-exemples.<langue>.md).

Sources (scripts/telecharger.sh) : les six treebanks UD latins, et, pour montrer la même phrase
avant conversion, le Latin Dependency Treebank 2.1 (format LDT, d'où vient UD_Latin-Perseus) et le
treebank PROIEL natif (d'où vient UD_Latin-PROIEL).

Pour chaque treebank, l'exemple est choisi parmi les phrases qui suivent l'analyse la plus fréquente
du treebank : c'est la pratique ordinaire de la norme qui est montrée, pas une exception.
"""

import collections
import csv
import glob
import html
import os
import re
import xml.etree.ElementTree as ET

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RACINE, ".cache")
SORTIE = os.path.join(RACINE, "generes")
TRADUCTIONS = os.path.join(RACINE, "scripts", "traductions.tsv")

TREEBANKS = ["CIRCSE", "Perseus", "PROIEL", "ITTB", "LLCT", "UDante"]
LICENCES = {"CIRCSE": "CC BY-SA 4.0", "Perseus": "CC BY-NC-SA 2.5", "PROIEL": "CC BY-NC-SA 3.0",
            "ITTB": "CC BY-NC-SA 3.0", "LLCT": "CC BY-SA 4.0", "UDante": "CC BY-NC-SA 3.0",
            "LDT": "CC BY-SA 3.0", "PROIEL natif": "CC BY-NC-SA 3.0"}
PAGES = {"CIRCSE": "circse", "Perseus": "perseus", "PROIEL": "proiel-ud", "ITTB": "ittb",
         "LLCT": "llct", "UDante": "udante", "LDT": "ldt", "PROIEL natif": "proiel"}

TEXTES = {
    "fr": {"dp": " :", "phrase": "phrase", "freq_tb": "Treebank", "freq_n": "Occurrences", "freq_an": "Analyses les plus fréquentes",
           "source": "Source", "licence": "licence", "conllu": "Lignes CoNLL-U",
           "natif": "La même phrase dans le format d'origine", "natif_lignes": "Lignes du fichier d'origine",
           "aucun": "Aucun exemple trouvé dans ce treebank.", "vide": "nœud vide", "norme": "page de la norme",
           "secondaire": "en pointillés sous la ligne : arêtes secondaires (slash) de PROIEL",
           "@hote": "hôte", "@autre": "autre mot", "@tete": "tête",
           "@part": "part.", "@nom": "nom", "@inf": "inf.", "@acc": "acc.",
           "@premier": "premier membre", "@suivant": "membre suivant", "@seule": "proposition seule",
           "@surnom": "nom", "@surverbe": "verbe", "@liaison": "relatif de liaison",
           "supplement": "autre analyse"},
    "en": {"dp": ":", "phrase": "sentence", "freq_tb": "Treebank", "freq_n": "Occurrences", "freq_an": "Most frequent analyses",
           "source": "Source", "licence": "licence", "conllu": "CoNLL-U lines",
           "natif": "The same sentence in the original format", "natif_lignes": "Lines of the original file",
           "aucun": "No example found in this treebank.", "vide": "empty node", "norme": "standard page",
           "secondaire": "dotted, below the line: PROIEL secondary edges (slashes)",
           "@hote": "host", "@autre": "other word", "@tete": "head",
           "@part": "part.", "@nom": "noun", "@inf": "inf.", "@acc": "acc.",
           "@premier": "first conjunct", "@suivant": "later conjunct", "@seule": "standalone clause",
           "@surnom": "noun", "@surverbe": "verb", "@liaison": "connecting relative",
           "supplement": "another analysis"},
}


# --- Lecture des données -------------------------------------------------------------------------

def lire_conllu(chemin, tb):
    phrases, lignes, meta = [], [], {}
    for l in open(chemin, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l:
            if lignes:
                phrases.append(phrase_ud(tb, lignes, meta))
            lignes, meta = [], {}
            continue
        lignes.append(l)
        if l.startswith("# ") and " = " in l:
            k, v = l[2:].split(" = ", 1)
            meta[k.strip()] = v
    if lignes:
        phrases.append(phrase_ud(tb, lignes, meta))
    return phrases


def phrase_ud(tb, lignes, meta):
    mots, mwt = [], set()
    for l in lignes:
        if l.startswith("#"):
            continue
        c = l.split("\t")
        if "-" in c[0]:
            a, b = c[0].split("-")
            mwt.update(range(int(a), int(b) + 1))
            continue
        if "." in c[0]:
            continue
        feats = dict(x.split("=", 1) for x in c[5].split("|")) if c[5] != "_" else {}
        mots.append({"id": int(c[0]), "forme": c[1], "lemme": c[2], "upos": c[3], "xpos": c[4],
                     "feats": feats, "tete": int(c[6]), "rel": c[7]})
    source = meta.get("source") or meta.get("reference") or meta.get("citation_hierarchy") or ""
    return {"tb": tb, "sent_id": meta.get("sent_id", ""), "texte": meta.get("text", ""),
            "mots": mots, "mwt": mwt, "lignes": lignes, "source": source}


def charger_ud():
    tbs = {}
    for tb in TREEBANKS:
        tbs[tb] = []
        for f in sorted(glob.glob(os.path.join(CACHE, "ud", f"UD_Latin-{tb}", "*.conllu"))):
            tbs[tb] += lire_conllu(f, tb)
    return tbs


def charger_ldt():
    """{(fichier, id de phrase): [mots]} du Latin Dependency Treebank 2.1."""
    ldt = {}
    for f in sorted(glob.glob(os.path.join(CACHE, "ldt", "v2.1", "Latin", "texts", "*.xml"))):
        nom = os.path.basename(f)
        for s in ET.parse(f).getroot().iter("sentence"):
            ldt[(nom, s.get("id"))] = {
                "doc": s.get("document_id", ""), "subdoc": s.get("subdoc", ""),
                "mots": [{"id": w.get("id"), "forme": w.get("form", ""), "lemme": w.get("lemma", ""),
                          "postag": w.get("postag", ""), "tete": w.get("head", ""),
                          "rel": w.get("relation", "")} for w in s.iter("word")]}
    return ldt


def charger_proiel():
    """{id de phrase: phrase} du treebank PROIEL natif, nœuds vides et arêtes secondaires compris."""
    proiel = {}
    for f in sorted(glob.glob(os.path.join(CACHE, "proiel", "*.xml"))):
        for div in ET.parse(f).getroot().iter("div"):
            titre = div.findtext("title", "")
            for s in div.iter("sentence"):
                proiel[s.get("id")] = {"titre": titre, "fichier": os.path.basename(f), "tokens": [
                    {"id": t.get("id"), "forme": t.get("form") or "∅" + t.get("empty-token-sort", ""),
                     "vide": t.get("empty-token-sort") is not None, "lemme": t.get("lemma", ""),
                     "pos": t.get("part-of-speech", ""), "morph": t.get("morphology", ""),
                     "tete": t.get("head-id"), "rel": t.get("relation", ""),
                     "slash": [(x.get("target-id"), x.get("relation")) for x in t.iter("slash")]}
                    for t in s.iter("token")]}
    return proiel


def charger_traductions():
    if not os.path.exists(TRADUCTIONS):
        return {}
    with open(TRADUCTIONS, encoding="utf-8") as f:
        return {(r["treebank"], r["sent_id"]): r for r in csv.DictReader(f, delimiter="\t")}


# --- Phénomènes ----------------------------------------------------------------------------------
# Chaque phénomène donne, pour une phrase UD, ses occurrences : (analyse, mots à mettre en évidence,
# bonus de choix d'exemple). L'analyse est écrite en notation UD, lisible dans les deux langues.

def enfants(p, m):
    return [k for k in p["mots"] if k["tete"] == m["id"]]


def par_id(p, i):
    return next((k for k in p["mots"] if k["id"] == i), None)


def copula(p):
    for m in p["mots"]:
        if m["lemme"] != "sum":
            continue
        if m["rel"].startswith(("cop", "aux")):
            analyse = f"sum : {m['rel']}"
        else:
            analyse = "sum : @tete"
        tete = par_id(p, m["tete"])
        bonus = (m["rel"] == "cop" and tete is not None and tete["upos"] == "ADJ"
                 and any(k["rel"] == "nsubj" for k in enfants(p, tete)))
        yield analyse, [m["id"]] + ([tete["id"]] if tete and m["rel"] == "cop" else []), bonus


def ablativus_absolutus(p):
    for m in p["mots"]:
        if m["feats"].get("VerbForm") != "Part" or m["feats"].get("Case") != "Abl":
            continue
        sujets = [k for k in enfants(p, m) if k["rel"].startswith("nsubj") and k["feats"].get("Case") == "Abl"]
        if sujets:
            yield (f"@part : {m['rel']} · @nom : {sujets[0]['rel']}", [m["id"], sujets[0]["id"]],
                   m["feats"].get("Aspect") == "Perf")


def accusativus_cum_infinitivo(p):
    for m in p["mots"]:
        if m["feats"].get("VerbForm") != "Inf":
            continue
        sujets = [k for k in enfants(p, m) if k["rel"].startswith("nsubj") and k["feats"].get("Case") == "Acc"]
        if sujets:
            tete = par_id(p, m["tete"])
            yield (f"@inf : {m['rel']} · @acc : {sujets[0]['rel']}", [m["id"], sujets[0]["id"]],
                   tete is not None and tete["upos"] == "VERB")


def gerundium_gerundivum(p):
    for m in p["mots"]:
        f = m["feats"]
        if f.get("VerbForm") in ("Ger", "Gdv"):
            forme = f"VerbForm={f['VerbForm']}"
        elif f.get("VerbForm") == "Part" and f.get("Aspect") == "Prosp" and f.get("Voice") == "Pass":
            forme = "VerbForm=Part + Aspect=Prosp"
        else:
            continue
        cas = [k for k in enfants(p, m) if k["upos"] == "ADP" and k["rel"] in ("case", "mark")]
        yield f"{m['upos']} {forme} : {m['rel']}", [m["id"]] + [k["id"] for k in cas], bool(cas)


def coordinatio(p):
    """L'enclitique -que : découpage (mot multi-token ou token séparé) et rattachement de cc, à son
    hôte (le mot qui le porte) ou à un autre mot. neque découpé en ne + que est laissé de côté."""
    for m in p["mots"]:
        if m["rel"] != "cc" or m["lemme"] != "que":
            continue
        tete, hote = par_id(p, m["tete"]), par_id(p, m["id"] - 1)
        if tete is None or (hote and hote["forme"].lower() in ("ne", "ni")):
            continue
        decoupe = "MWT" if m["id"] in p["mwt"] else "token"
        cote = "conj" if tete["rel"].startswith("conj") else tete["rel"]
        sur = "@hote" if hote and hote["id"] == tete["id"] else "@autre"
        yield (f"que ({decoupe}) : cc → {sur} ({cote})",
               [m["id"], tete["id"]] + ([hote["id"]] if hote and hote["id"] != tete["id"] else []),
               tete["rel"].startswith("conj"))


PROPOSITIONS = ("root", "conj", "parataxis", "ccomp", "csubj", "advcl", "acl")


def sine_verbo(p):
    """Proposition sans verbe ni sum (omnia praeclara rara) : un mot qui n'est ni verbe ni auxiliaire,
    sans cop ni aux, a un sujet nsubj et occupe une place de proposition. L'ablatif absolu nominal
    (Caesare duce) est laissé de côté. L'analyse est la catégorie de la tête, et son cas s'il n'est
    pas le nominatif."""
    for m in p["mots"]:
        if m["upos"] in ("VERB", "AUX") or m["rel"] == "advcl:abs" or m["rel"].split(":")[0] not in PROPOSITIONS:
            continue
        ch = enfants(p, m)
        if any(k["rel"] == "cop" or k["rel"].startswith("aux") for k in ch):
            continue
        sujets = [k for k in ch if k["rel"] == "nsubj"]
        if not sujets:
            continue
        # Verbe écrit dans un membre suivant qui partage le sujet (robustius sed minus refundet) :
        # c'est l'ellipse d'un verbe plein, non une proposition sans verbe.
        if any(k["rel"].startswith("conj") and k["upos"] == "VERB"
               and not any(x["rel"].startswith("nsubj") for x in enfants(p, k)) for k in ch):
            continue
        cas = m["feats"].get("Case", "Nom")
        tete = m["upos"] + (f" {cas}" if m["upos"] != "ADV" and cas != "Nom" else "")
        yield (f"@tete : {tete}", [m["id"], sujets[0]["id"]],
               m["rel"] == "root" and m["upos"] == "ADJ" and sujets[0]["upos"] == "NOUN")


def ellipsis(p):
    """Ellipse du verbe : chaque mot qui porte des orphan (le reste promu tête de la proposition
    elliptique), avec la place de cette proposition : premier membre d'une coordination dont un membre
    suivant a le verbe, membre suivant (conj), proposition seule (racine sans conj), ou autre relation."""
    for h in p["mots"]:
        orphelins = [k for k in enfants(p, h) if k["rel"] == "orphan"]
        if not orphelins:
            continue
        if h["rel"] == "root":
            place = "root (@premier)" if any(k["rel"].startswith("conj") for k in enfants(p, h)) else "root (@seule)"
        elif h["rel"].startswith("conj"):
            place = "conj (@suivant)"
        else:
            place = h["rel"]
        yield f"orphan → {place}", [h["id"]] + [k["id"] for k in orphelins], h["upos"] in ("NOUN", "PROPN")


# Verbes qui régissent un cas autre que l'accusatif, lemmes ramenés en minuscules et en u/i.
REGIMES = {
    "Abl": {"utor", "abutor", "fruor", "fungor", "potior", "uescor", "careo", "egeo", "indigeo"},
    "Gen": {"obliuiscor", "memini", "reminiscor", "misereor"},
    "Dat": {"parco", "impero", "noceo", "faueo", "pareo", "resisto", "obsequor", "studeo", "inuideo",
            "ignosco", "persuadeo", "obtempero", "subuenio", "medeor"},
}


def u_i(lemme):
    return lemme.lower().replace("v", "u").replace("j", "i")


def obliqui(p):
    """Complément sans préposition d'un verbe qui régit l'ablatif, le génitif ou le datif (REGIMES) :
    relation donnée à ce complément."""
    for m in p["mots"]:
        cas = m["feats"].get("Case")
        if cas not in REGIMES or m["upos"] not in ("NOUN", "PROPN", "PRON", "DET", "ADJ"):
            continue
        h = par_id(p, m["tete"]) if m["tete"] else None
        if h is None or h["upos"] != "VERB" or u_i(h["lemme"]) not in REGIMES[cas]:
            continue
        if any(k["upos"] == "ADP" for k in enfants(p, m)):
            continue
        yield f"{cas} : {m['rel']}", [h["id"], m["id"]], h["feats"].get("VerbForm") == "Fin" and m["upos"] == "NOUN"


NOMINAUX = ("NOUN", "PROPN", "PRON", "DET", "ADJ", "NUM")


def participium(p):
    """Participe employé seul, hors périphrases (avec aux ou cop), ablatif absolu, racine et conjoint ;
    l'adjectif verbal et le gérondif (que ITTB et Perseus codent Part + Aspect=Prosp) sont laissés de
    côté. Analyse : relation du participe et catégorie de sa tête."""
    for m in p["mots"]:
        f = m["feats"]
        if f.get("VerbForm") != "Part" or (f.get("Aspect") == "Prosp" and f.get("Voice") != "Act"):
            continue
        if m["rel"] in ("root", "advcl:abs") or m["rel"].startswith("conj"):
            continue
        if any(k["rel"] == "cop" or k["rel"].startswith("aux") for k in enfants(p, m)):
            continue
        h = par_id(p, m["tete"])
        sur = "@surnom" if h["upos"] in NOMINAUX else "@surverbe" if h["upos"] in ("VERB", "AUX") else h["upos"]
        yield f"{m['rel']} → {sur}", [m["id"], h["id"]], m["rel"] in ("acl", "amod", "advcl", "advcl:pred")


def predicat(p, m):
    """Le prédicat de la proposition qui contient m : le premier mot, en remontant depuis la tête de m,
    qui est un verbe ou porte une copule."""
    x = par_id(p, m["tete"]) if m["tete"] else None
    while x is not None:
        if x["upos"] in ("VERB", "AUX") or any(k["rel"] == "cop" for k in enfants(p, x)):
            return x
        x = par_id(p, x["tete"]) if x["tete"] else None
    return None


def relativa(p):
    """Proposition relative : pour chaque relatif (qui, quicumque, PronType=Rel), le prédicat de sa
    proposition, sa relation et la catégorie de sa tête (nom : relative à antécédent ; verbe : relative
    sans antécédent, le plus souvent). Une relative coordonnée (conj) est laissée de côté ; une relative
    racine de la phrase est un relatif de liaison (Quae cum ita sint)."""
    for r in p["mots"]:
        if u_i(r["lemme"]) not in ("qui", "quicumque") or r["feats"].get("PronType") != "Rel":
            continue
        c = predicat(p, r)
        if c is None or c["rel"].startswith("conj"):
            continue
        if c["rel"] == "root":
            yield "root (@liaison)", [r["id"], c["id"]], False
            continue
        h = par_id(p, c["tete"])
        sur = "@surnom" if h["upos"] in NOMINAUX else "@surverbe" if h["upos"] in ("VERB", "AUX") else h["upos"]
        yield f"{c['rel']} → {sur}", [r["id"], c["id"]], h["upos"] == "NOUN" and c["rel"].startswith("acl")


# Verbes de demande, d'ordre, d'effort et de crainte, construits avec ut ou ne + subjonctif.
VERBA_UT = {"rogo", "oro", "postulo", "precor", "obsecro", "flagito", "exoro", "impetro", "impero",
            "praecipio", "edico", "decerno", "statuo", "moneo", "admoneo", "hortor", "persuadeo",
            "suadeo", "efficio", "perficio", "curo", "caueo", "permitto", "timeo", "metuo", "uereor"}


def ut_completiva(p):
    """Proposition en ut, uti ou ne au subjonctif qui dépend d'un verbe de VERBA_UT : sa relation."""
    for m in p["mots"]:
        if m["upos"] not in ("VERB", "AUX") or m["feats"].get("Mood") != "Sub" or not m["tete"]:
            continue
        mk = [k for k in enfants(p, m) if k["rel"] == "mark" and u_i(k["lemme"]) in ("ut", "uti", "ne")]
        h = par_id(p, m["tete"])
        if mk and h["upos"] == "VERB" and u_i(h["lemme"]) in VERBA_UT:
            yield m["rel"], [h["id"], mk[0]["id"], m["id"]], h["feats"].get("VerbForm") == "Fin"


PHENOMENES = {
    "copula": copula,
    "ablativus-absolutus": ablativus_absolutus,
    "accusativus-cum-infinitivo": accusativus_cum_infinitivo,
    "gerundium-gerundivum": gerundium_gerundivum,
    "coordinatio": coordinatio,
    "sine-verbo": sine_verbo,
    "ellipsis": ellipsis,
    "obliqui": obliqui,
    "participium": participium,
    "relativa": relativa,
    "ut-completiva": ut_completiva,
}

# Exemples supplémentaires, pour une analyse qui n'est pas la plus fréquente du treebank mais que la
# fiche discute : (treebank, analyse, filtre sur la phrase).
SUPPLEMENTS = {
    "sine-verbo": [("CIRCSE", "@tete : NOUN Dat", lambda p: "Tacitus" in p["sent_id"])],
    "ellipsis": [("CIRCSE", "orphan → root (@premier)", lambda p: "Tacitus" in p["sent_id"])],
    "participium": [("Perseus", "amod → @surnom", lambda p: p["sent_id"].startswith("phi0474.phi013"))],
    "relativa": [("Perseus", "acl:relcl → @surverbe", lambda p: p["sent_id"].startswith("phi0631.phi001"))],
}


# --- Choix des exemples --------------------------------------------------------------------------

def propre(p):
    return all(not re.search(r"\d", m["forme"]) for m in p["mots"])


def formulaire(p):
    """Formules et anonymisations des chartes (LLCT) : gardées en dernier recours."""
    return (p["texte"].lstrip().startswith(("+", "signum")) or "[" in p["texte"]
            or "supra legitur" in p["texte"] or "super legitur" in p["texte"])


def choisir(phrases, fonction, analyse_cible, existe=lambda p: True):
    candidats = []
    for p in phrases:
        n = sum(1 for m in p["mots"] if m["upos"] != "PUNCT")
        if not propre(p) or not existe(p):
            continue
        for analyse, cibles, bonus in fonction(p):
            if analyse == analyse_cible:
                ecart = 0 if 6 <= n <= 14 else min(abs(n - 6), abs(n - 14))
                candidats.append(((ecart, formulaire(p), not bonus, abs(n - 9), p["sent_id"]), p, cibles))
                break
    if not candidats:
        return None, []
    _, p, cibles = min(candidats, key=lambda c: c[0])
    return p, cibles


# --- Dessin des arbres en SVG --------------------------------------------------------------------

def niveaux(arcs):
    """Hauteur de chaque arc : un de plus que le plus haut des arcs qu'il couvre."""
    ordre = sorted(range(len(arcs)), key=lambda i: abs(arcs[i][1] - arcs[i][0]))
    niv = [0] * len(arcs)
    for i in ordre:
        a, b = sorted(arcs[i][:2])
        dedans = [niv[j] for j in ordre if j != i and niv[j] and a <= min(arcs[j][:2]) and max(arcs[j][:2]) <= b]
        niv[i] = 1 + max(dedans, default=0)
    return niv


def svg(noeuds, cibles=(), secondaires=()):
    """noeuds : [(clé, forme, étiquette sous la forme, clé de la tête ou None, relation)] dans l'ordre ;
    secondaires : [(clé de la tête, clé du dépendant, relation)], dessinées sous la ligne."""
    pos = {}
    x = 10
    largeurs = []
    for cle, forme, sous, _, _ in noeuds:
        l = max(len(forme) * 8.2, len(sous) * 6.4) + 18
        largeurs.append(l)
        pos[cle] = x + l / 2
        x += l
    largeur = x + 10
    arcs = [(pos[t], pos[c], rel) for c, _, _, t, rel in noeuds if t is not None and t in pos]
    racines = [(pos[c], rel) for c, _, _, t, rel in noeuds if t is None or t not in pos]
    sec = [(pos[t], pos[d], rel) for t, d, rel in secondaires if t in pos and d in pos]
    niv, niv_sec = niveaux(arcs), niveaux(sec)
    pas = 26
    haut = (max(niv, default=0) + 1) * pas + 16
    base = haut + 14
    bas = base + 22 + (max(niv_sec, default=0) * pas + 14 if sec else 0)
    out = [f'<svg class="arbre" xmlns="http://www.w3.org/2000/svg" width="{largeur:.0f}" height="{bas:.0f}" '
           f'viewBox="0 0 {largeur:.0f} {bas:.0f}" role="img">']
    for (xt, xd, rel), n in zip(arcs, niv):
        y = base - 14 - n * pas
        dx = 4 if xd > xt else -4
        out.append(f'<path class="arc" d="M{xt + dx:.1f},{base - 14} L{xt + dx:.1f},{y} L{xd:.1f},{y} L{xd:.1f},{base - 16}"/>')
        out.append(f'<path class="pointe" d="M{xd - 3.5:.1f},{base - 22} L{xd:.1f},{base - 15} L{xd + 3.5:.1f},{base - 22} Z"/>')
        out.append(etiquette((xt + xd) / 2, y, rel))
    for xr, rel in racines:
        out.append(f'<path class="arc" d="M{xr:.1f},8 L{xr:.1f},{base - 16}"/>')
        out.append(f'<path class="pointe" d="M{xr - 3.5:.1f},{base - 22} L{xr:.1f},{base - 15} L{xr + 3.5:.1f},{base - 22} Z"/>')
        out.append(etiquette(xr, 12, rel))
    for (xt, xd, rel), n in zip(sec, niv_sec):
        y = base + 22 + n * pas
        out.append(f'<path class="arc secondaire" d="M{xt:.1f},{base + 10} L{xt:.1f},{y} L{xd:.1f},{y} L{xd:.1f},{base + 10}"/>')
        out.append(etiquette((xt + xd) / 2, y, rel))
    for (cle, forme, sous, _, _), l in zip(noeuds, largeurs):
        classe = "forme cible" if cle in cibles else "forme"
        out.append(f'<text class="{classe}" x="{pos[cle]:.1f}" y="{base}" text-anchor="middle">{html.escape(forme)}</text>')
        if sous:
            out.append(f'<text class="sous" x="{pos[cle]:.1f}" y="{base + 13}" text-anchor="middle">{html.escape(sous)}</text>')
    out.append("</svg>")
    return "".join(out)


def etiquette(x, y, texte):
    l = len(texte) * 6.4 + 6
    return (f'<rect class="fond" x="{x - l / 2:.1f}" y="{y - 7}" width="{l:.1f}" height="13" rx="3"/>'
            f'<text class="rel" x="{x:.1f}" y="{y + 3.5}" text-anchor="middle">{html.escape(texte)}</text>')


def svg_ud(p, cibles):
    return svg([(m["id"], m["forme"], m["upos"], m["tete"] or None, m["rel"]) for m in p["mots"]], set(cibles))


def svg_ldt(phrase, cibles):
    return svg([(w["id"], w["forme"], w["postag"], w["tete"] if w["tete"] not in ("", "0") else None, w["rel"])
                for w in phrase["mots"]], set(cibles))


def svg_proiel(phrase, cibles):
    toks = phrase["tokens"]
    noeuds = [(t["id"], t["forme"], t["pos"] if not t["vide"] else "", t["tete"], t["rel"]) for t in toks]
    noeuds = [n for n, t in zip(noeuds, toks) if not t["vide"]] + [n for n, t in zip(noeuds, toks) if t["vide"]]
    sec = [(t["id"], cible, rel) for t in toks for cible, rel in t["slash"]]
    return svg(noeuds, set(cibles), sec)


# --- Écriture des fragments ----------------------------------------------------------------------

def libelle(analyse, t):
    for cle in ("@hote", "@autre", "@tete", "@part", "@nom", "@inf", "@acc", "@premier", "@suivant", "@seule", "@surnom", "@surverbe", "@liaison"):
        analyse = analyse.replace(cle, t[cle])
    return analyse.replace("|", "/")


def bloc(titre, lignes):
    corps = "\n".join("        " + l for l in lignes)
    return f'??? note "{titre}"\n\n    ```text\n{corps}\n    ```\n'


def citation(p):
    return f"`{p['sent_id']}`" + (f" ({p['source']})" if p["source"] and p["source"] != p["sent_id"] else "")


def traduction(tr, tb, sent_id, langue):
    r = tr.get((tb, sent_id))
    if not (r and r.get(langue)):
        return ""
    return f"\n*« {r[langue]} »*\n" if langue == "fr" else f"\n*“{r[langue]}”*\n"


def lignes_ldt(phrase):
    return [f"{w['id']}\t{w['forme']}\t{w['lemme']}\t{w['postag']}\t{w['tete']}\t{w['rel']}" for w in phrase["mots"]]


def lignes_proiel(phrase):
    out = []
    for t in phrase["tokens"]:
        sl = " ".join(f"slash:{r}→{c}" for c, r in t["slash"])
        out.append("\t".join([t["id"], t["forme"], t["lemme"] or "_", t["pos"] or "_", t["morph"] or "_",
                              t["tete"] or "_", t["rel"]] + ([sl] if sl else [])))
    return out


def ecrire(slug, tbs, ldt, proiel, tr):
    fonction = PHENOMENES[slug]
    supplements = SUPPLEMENTS.get(slug, [])
    stats = {}
    for tb in TREEBANKS:
        c = collections.Counter()
        for p in tbs[tb]:
            for analyse, _, _ in fonction(p):
                c[analyse] += 1
        stats[tb] = c

    exemples = {}
    for tb in TREEBANKS:
        if not stats[tb]:
            exemples[tb] = (None, [])
            continue
        existe = lambda p: True
        if tb == "Perseus":
            existe = lambda p: tuple(p["sent_id"].split("@")) in ldt
        elif tb == "PROIEL":
            existe = lambda p: p["sent_id"] in proiel
        exemples[tb] = choisir(tbs[tb], fonction, stats[tb].most_common(1)[0][0], existe)

    for langue, t in TEXTES.items():
        lignes = [f"| {t['freq_tb']} | {t['freq_n']} | {t['freq_an']} |", "|---|---:|---|"]
        for tb in TREEBANKS:
            total = sum(stats[tb].values())
            if not total:
                lignes.append(f"| [{tb}](../normes/{PAGES[tb]}.md) | 0 | — |")
                continue
            top = " ; ".join(f"`{libelle(a, t)}` {100 * n / total:.0f} %" for a, n in stats[tb].most_common(4))
            lignes.append(f"| [{tb}](../normes/{PAGES[tb]}.md) | {total} | {top} |")
        with open(os.path.join(SORTIE, f"{slug}-frequences.{langue}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lignes) + "\n")

        out = []
        for tb in TREEBANKS:
            p, cibles = exemples[tb]
            out.append(f"### {tb}\n")
            if p is None:
                out.append(f"{t['aucun']}\n")
                continue
            exemple(out, tb, p, cibles, t, langue, ldt, proiel, tr)
        for tb, analyse, filtre in supplements:
            p, cibles = choisir([q for q in tbs[tb] if filtre(q)], fonction, analyse)
            if p is not None:
                out.append(f"### {tb}{t['dp']} {t['supplement']} (`{libelle(analyse, t)}`)\n")
                exemple(out, tb, p, cibles, t, langue, ldt, proiel, tr)
        with open(os.path.join(SORTIE, f"{slug}-exemples.{langue}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(out))
    return {tb: (exemples[tb][0] or {}).get("sent_id") for tb in TREEBANKS}


def exemple(out, tb, p, cibles, t, langue, ldt, proiel, tr):
    """Une phrase UD : texte, traduction, source, arbre, lignes CoNLL-U et, pour Perseus et PROIEL, la
    même phrase dans son format d'origine."""
    out.append(f"> {html.escape(p['texte'])}\n")
    out.append(traduction(tr, tb, p["sent_id"], langue))
    out.append(f"{t['source']}{t['dp']} UD_Latin-{tb} r2.18, {citation(p)} — {t['licence']} {LICENCES[tb]} "
               f"— [{t['norme']}](../normes/{PAGES[tb]}.md)\n")
    out.append(f'<div class="arbre-cadre">{svg_ud(p, cibles)}</div>\n')
    out.append(bloc(t["conllu"], p["lignes"]))
    if tb == "Perseus":
        cle = tuple(p["sent_id"].split("@"))
        nat = ldt[cle]
        ids = [str(i) for i in cibles] if len(nat["mots"]) == len(p["mots"]) else []
        out.append(f"#### {t['natif']}{t['dp']} LDT 2.1\n")
        out.append(f"{t['source']}{t['dp']} Latin Dependency Treebank 2.1, `{cle[0]}`, {t['phrase']} {cle[1]}"
                   f" ({nat['subdoc']}) — {t['licence']} {LICENCES['LDT']} — [{t['norme']}](../normes/ldt.md)\n")
        out.append(f'<div class="arbre-cadre">{svg_ldt(nat, ids)}</div>\n')
        out.append(bloc(t["natif_lignes"], lignes_ldt(nat)))
    if tb == "PROIEL":
        nat = proiel[p["sent_id"]]
        reels = [x["id"] for x in nat["tokens"] if not x["vide"]]
        ids = [reels[i - 1] for i in cibles if i <= len(reels)] if len(reels) == len(p["mots"]) else []
        out.append(f"#### {t['natif']}{t['dp']} PROIEL\n")
        out.append(f"{t['source']}{t['dp']} PROIEL treebank, `{nat['fichier']}`, {t['phrase']} {p['sent_id']}"
                   f" ({nat['titre']}) — {t['licence']} {LICENCES['PROIEL natif']} "
                   f"— [{t['norme']}](../normes/proiel.md). ∅ = {t['vide']}{';' if t['dp'] == ':' else ' ;'} {t['secondaire']}.\n")
        out.append(f'<div class="arbre-cadre">{svg_proiel(nat, ids)}</div>\n')
        out.append(bloc(t["natif_lignes"], lignes_proiel(nat)))


def main():
    os.makedirs(SORTIE, exist_ok=True)
    tbs, ldt, proiel, tr = charger_ud(), charger_ldt(), charger_proiel(), charger_traductions()
    for slug in PHENOMENES:
        choix = ecrire(slug, tbs, ldt, proiel, tr)
        print(slug, choix)


if __name__ == "__main__":
    main()
