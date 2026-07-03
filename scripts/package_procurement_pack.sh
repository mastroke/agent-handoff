#!/usr/bin/env bash
# Package the Agency Handoff procurement pack into a Gumroad-ready zip.
# Run from anywhere; writes dist/agency-handoff-pack.zip.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PACK="$ROOT/pack/procurement"
DIST="$ROOT/dist"
VERSION="$(git -C "$ROOT" describe --tags --always 2>/dev/null || echo 0.1.0)"
STAGE="$DIST/agency-handoff-pack-$VERSION"
OUT="$ROOT/dist/agency-handoff-pack.zip"

rm -rf "$STAGE" "$OUT"
mkdir -p "$STAGE"
cp -r "$PACK"/* "$STAGE"/
# Bundle the OSS CLI quickstart + the parent README so the pack is self-contained.
cp "$ROOT/README.md" "$STAGE/agent-handoff-README.md"
cat > "$STAGE/INSTALL.md" <<EOF
# Agency Handoff Pack — $VERSION

You bought the pack. The OSS CLI that pairs with these templates is free:

    pip install agent-handoff
    agent-handoff run examples/agency-handoff/scenarios.yaml
    agent-handoff report examples/agency-handoff/scenarios.results.json --pack -o handoff-report.md

Copy sow-snippet.md into your statement of work; attach the generated
handoff-report.md at client sign-off. See agent-handoff-README.md for the
full cross-layer model (prompt / tool / memory / retrieval).

Want the governed-memory gate too (EU AI Act acceptance packs)?
https://github.com/mastroke/agent-acceptance
EOF

(cd "$DIST" && zip -qr "$(basename "$OUT")" "$(basename "$STAGE")")
rm -rf "$STAGE"
echo "Wrote $OUT  ($(du -h "$OUT" | cut -f1))"
