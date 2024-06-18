#!/bin/bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  . .venv/bin/activate
fi

rm -Rf python/src/omotes_sdk_protocol/
mkdir -p python/src/omotes_sdk_protocol/
protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/job.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/job.proto
protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/work_flow.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/work_flow.proto
touch python/src/omotes_sdk_protocol/__init__.py
touch python/src/omotes_sdk_protocol/py.typed
