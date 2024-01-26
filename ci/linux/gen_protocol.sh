#!/bin/bash

. .venv/bin/activate
rm -Rf python/src/omotes_sdk_protocol/
mkdir -p python/src/omotes_sdk_protocol/
protoc -I src/ --python_out python/src/omotes_sdk_protocol/ ./src/job.proto
protoc -I src/ --mypy_out python/src/omotes_sdk_protocol/ ./src/job.proto
touch python/src/omotes_sdk_protocol/__init__.py
