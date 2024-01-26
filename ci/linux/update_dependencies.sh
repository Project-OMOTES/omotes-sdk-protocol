#!/usr/bin/env sh

. .venv/bin/activate
pip-compile --output-file=requirements.txt pyproject.toml
pip-compile --extra=dev -c requirements.txt --output-file=dev-requirements.txt pyproject.toml
