#!/usr/bin/node

const myArgs = process.argv.slice(2);

if (process.argv[2] && isNaN(process.argv[2]) === false) {
  console.log('My number: ' + parseInt(myArgs[0]));
} else {
  console.log('Not a number');
}
