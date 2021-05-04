#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const myargs = process.argv.slice(2);

fs.readFile(myargs[0], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
