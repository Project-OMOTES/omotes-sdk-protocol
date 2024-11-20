#!/bin/bash

if [[ "$OSTYPE" != "win32" && "$OSTYPE" != "msys" ]]; then
  . .venv/bin/activate
fi

rm -Rf python/src/omotes_sdk_protocol/
mkdir -p python/src/omotes_sdk_protocol/
protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/job.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/job.proto
protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/workflow.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/workflow.proto
touch python/src/omotes_sdk_protocol/__init__.py
touch python/src/omotes_sdk_protocol/py.typed

protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/internal/task.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/internal/task.proto
protoc -I include/ -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/internal/task.proto
protoc -I include/ -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/internal/task.proto
touch python/src/omotes_sdk_protocol/internal/__init__.py
touch python/src/omotes_sdk_protocol/internal/py.typed

sed -i 's/import job_pb2/from .. import job_pb2/g' python/src/omotes_sdk_protocol/internal/task_pb2.py
sed -i 's/import job_pb2/from .. import job_pb2/g' python/src/omotes_sdk_protocol/internal/task_pb2.pyi
