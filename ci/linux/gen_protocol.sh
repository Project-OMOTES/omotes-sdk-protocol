#!/bin/bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  . .venv/bin/activate
fi

rm -Rf python/src/omotes_sdk_protocol/
mkdir -p python/src/omotes_sdk_protocol/
protoc -I include/ -I src/ --python_out python/src/ --mypy_out python/src/ omotes_sdk_protocol/job.proto omotes_sdk_protocol/workflow.proto omotes_sdk_protocol/internal/task.proto
touch python/src/omotes_sdk_protocol/internal/__init__.py
touch python/src/omotes_sdk_protocol/__init__.py
touch python/src/omotes_sdk_protocol/py.typed
