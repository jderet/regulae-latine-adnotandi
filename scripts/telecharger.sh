#!/bin/sh
# Télécharge, à des versions figées, les données dont sont tirés les exemples (dans .cache/, hors dépôt).
set -e
RACINE=$(cd "$(dirname "$0")/.." && pwd)
CACHE="$RACINE/.cache"
UD_VERSION=r2.18
LDT_COMMIT=bf4334f0af5e13d16b04c1cccd6237e683ac6f5f
PROIEL_COMMIT=8e388967a1335ed12335ddc655fe46993ee7d57a
mkdir -p "$CACHE"

for t in CIRCSE ITTB LLCT PROIEL Perseus UDante; do
  [ -d "$CACHE/ud/UD_Latin-$t" ] || git -c advice.detachedHead=false clone -q --depth 1 --branch "$UD_VERSION" \
    "https://github.com/UniversalDependencies/UD_Latin-$t.git" "$CACHE/ud/UD_Latin-$t"
done

# Latin Dependency Treebank 2.1 (format LDT d'origine, dont vient UD_Latin-Perseus)
if [ ! -d "$CACHE/ldt" ]; then
  git clone -q --filter=blob:none --no-checkout https://github.com/PerseusDL/treebank_data.git "$CACHE/ldt"
  git -C "$CACHE/ldt" sparse-checkout set v2.1/Latin
  git -C "$CACHE/ldt" -c advice.detachedHead=false checkout -q "$LDT_COMMIT"
fi

# PROIEL (format XML d'origine, dont vient UD_Latin-PROIEL)
if [ ! -d "$CACHE/proiel" ]; then
  mkdir -p "$CACHE/proiel"
  for f in latin-nt caes-gal cic-att cic-off pal-agr per-aeth; do
    curl -sSfL -o "$CACHE/proiel/$f.xml" \
      "https://raw.githubusercontent.com/proiel/proiel-treebank/$PROIEL_COMMIT/$f.xml"
  done
fi
echo "Données prêtes dans $CACHE"
