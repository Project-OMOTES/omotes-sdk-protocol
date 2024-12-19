#!/usr/bin/env bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  echo "Activating .venv first."
  . ./python/.venv/bin/activate
fi
pip-sync ./python/dev-requirements.txt ./python/requirements.txt
