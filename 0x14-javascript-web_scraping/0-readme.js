#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const myargs = process.argv.slice(2);

fs.readFile(myargs[0], (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});
