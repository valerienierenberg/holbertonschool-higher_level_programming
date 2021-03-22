#!/usr/bin/node

const myArgs = process.argv.slice(2);
let i;

if (!myArgs[0] || !parseInt(myArgs[0])) {
  console.log('Missing size');
} else {
  for (i = 0; i < myArgs; i++) {
    console.log('X'.repeat(myArgs[0]));
  }
}
