#!/bin/sh

set -e
set -x

LATEST=$1
if [ ! $LATEST ]; then
  LATEST="3.48.4"
fi

PROJECT="iterative/dvc"
GHAPI_URL="https://api.github.com/repos/$PROJECT/releases/latest"
LATEST="3.48.4"

sed -i 's/^VERSION = .*$/VERSION = '"\"$LATEST\""'/g' download.py
