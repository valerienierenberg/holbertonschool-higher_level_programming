#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, function (err, dataA) {
  if (err) throw err;
  fs.readFile(fileB, function (err, dataB) {
    if (err) throw err;
    fs.appendFile(fileC, dataA + dataB, function (err) {
      if (err) throw err;
    });
  });
});
