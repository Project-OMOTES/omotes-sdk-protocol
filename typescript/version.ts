import { readFileSync, writeFileSync } from 'fs';

const packageJson = JSON.parse(readFileSync('./package.json', 'utf8'));
const newVersion = process.argv[2];
packageJson.version = newVersion;
writeFileSync('./package.json', JSON.stringify(packageJson, null, 2), 'utf8');