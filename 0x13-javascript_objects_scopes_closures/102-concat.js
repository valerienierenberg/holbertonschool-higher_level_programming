#!/usr/bin/node

// cat *.txt >> all.txt

var concat = require('concat-files');
const myArgs = process.argv.slice(2);

  concat([
    myArgs[0],
    myArgs[1],
    myArgs[2],
  ], myArgs[3], function(err) {
    if (err) throw err
    console.log('done');
  });
