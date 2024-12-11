#!/usr/bin/env bash

python3 -m venv ./python/.venv
if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  echo "Activating .venv first."
  . ./python/.venv/bin/activate
fi
pip3 install pip-tools
