#!/usr/bin/env bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  echo "Activating .venv first."
  . .venv/bin/activate
fi

pip-compile --upgrade --output-file=requirements.txt pyproject.toml
pip-compile --upgrade --extra=dev -c requirements.txt --output-file=dev-requirements.txt pyproject.toml
