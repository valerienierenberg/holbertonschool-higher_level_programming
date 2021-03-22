#!/usr/bin/node

const myArgs = process.argv.slice(2);

function add (a, b) {
  console.log(parseInt(myArgs[0]) + parseInt(myArgs[1]));
}

add();
