# @omotes/proto

Library containing generated OMOTES Job class from Protobuf specification.

You probably don't want to install this directly, rather install it through [@omotes/sdk](https://npmjs.com/@omotes/sdk).

## Development

Make sure you have the `protoc` executable available on your PATH.
Version 25.2 is used: https://github.com/protocolbuffers/protobuf/releases.

### Building

Run the following command to build the protobuf artifacts:

```sh
npm run build
```

### Bumping version from tag

To correctly version `package.json` with the corresponding git tag, run:

```sh
npm run set-version major.minor.patch
```

You shouldn't have to run this yourself, it will be called through GitHub actions (see [node_release.yml](../.github/workflows/node_release.yml)).