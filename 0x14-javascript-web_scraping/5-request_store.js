#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, res, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(filename, body, 'utf8');
  }
});
