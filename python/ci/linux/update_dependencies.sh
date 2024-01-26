#!/usr/bin/env sh

. ./python/.venv/bin/activate
pip-compile --output-file=./python/requirements.txt ./python/pyproject.toml
pip-compile --extra=dev -c ./python/requirements.txt --output-file=./python/dev-requirements.txt ./python/pyproject.toml
