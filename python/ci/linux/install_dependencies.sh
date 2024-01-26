#!/usr/bin/env sh

. ./python/.venv/bin/activate
pip-sync ./python/dev-requirements.txt ./python/requirements.txt
