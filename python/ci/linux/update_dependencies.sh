#!/usr/bin/env bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  echo "Activating .venv first."
  . ./python/.venv/bin/activate
fi

pip-compile --upgrade --output-file=./python/requirements.txt ./python/pyproject.toml
pip-compile --upgrade --extra=dev -c ./python/requirements.txt --output-file=./python/dev-requirements.txt ./python/pyproject.toml
