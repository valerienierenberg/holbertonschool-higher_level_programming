#!/usr/bin/node

const myArgs = process.argv.slice(2);
const num = parseInt(myArgs[0]);
let i;

if (!num) {
  console.log('Missing number of occurrences');
} for (i = 0; i < num; i++) {
  console.log('C is fun');
}
