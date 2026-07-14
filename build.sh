#!/bin/bash
# Build script for Elekio website with Eleventy
# Usage: ./build.sh [--serve]

NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

cd "$(dirname "$0")"

if [ "$1" == "--serve" ]; then
  echo "🚀 Elekio — Mode développement sur http://localhost:8080"
  npx @11ty/eleventy --serve
else
  echo "🔧 Elekio — Build de production"
  rm -rf _site
  npx @11ty/eleventy
  echo "✅ Build terminé — _site/ prêt pour déploiement"
fi
