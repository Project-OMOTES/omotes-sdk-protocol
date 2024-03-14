import { exec } from 'node:child_process';

const options = [
  `--plugin=protoc-gen-ts="./node_modules/.bin/protoc-gen-ts"`,
  `--experimental_allow_proto3_optional`,
  `--ts_opt=esModuleInterop=true`,
  `--js_out="import_style=commonjs,binary:./src"`,
  `--ts_out="./src"`,
  `--proto_path="../src"`,
  `job.proto`
];

const script = `protoc ${options.join(' ')}`;
exec(script, (err, stdout, stderr) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log('Successfully generated typescript files.');
  process.exit(0);
});