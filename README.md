# OMOTES orchestrator

This repository is part of the 'Nieuwe Warmte Nu Design Toolkit' project. 

Orchestrator component of OMOTES project which monitors workflows and starts the various steps of each workflow.


# Developers Guide
Please install `protoc` on your machine and make sure it is available in your `PATH`.  
Version 25.2 is used: https://github.com/protocolbuffers/protobuf/releases.

The protobuf definition is under `src/` and any language specific generated code resides under the language
folder. For instance, the Python implementation resides under `python/`. The same holds for any packaging
and build tools, they reside under the language folder as well. The tools for generating the language-specific
code us under root `/`.

To generate new language-specific implementations of the protocol:
- Alter the protobuf defintions under `src/`.
- Run `ci/linux/create_venv.sh` and `ci/linux/install_dependencies.sh` to create a Python environment in
  which `protoc` plugins are installed.
- Run `ci/linux/gen_protocol.sh` to generate the language-specific implementations.

# Python-specific implementation Developers Guide
A number of tools are available to create the Python package:
- `./python/ci/linux/create_venv.sh`: Creates a virtualenvironment specific to the Python implementation of the 
   generated protobuf messages under `./python/.venv/`.
- `./python/ci/linux/install_dependencies.sh`: Installs the build and package dependencies in `./python/.venv/`.
- `./python/ci/linux/update_dependencies.sh`: Updates the build and package dependencies.
- `./python/ci/linux/build_python_package.sh`: Generates the python package containing the python generated protobuf
  messages.

# TypeScript-specific implementation Developers Guide
To build the TypeScript artifacts, navigate to `/typescript` and run `npm run build`. Versioning is done automatically
through the corresponding GitHub action (see [node_release.yml](./.github/workflows/node_release.yml)).