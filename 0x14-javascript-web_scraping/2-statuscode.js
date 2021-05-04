#!/usr/bin/node

const request = require('request');
const process = require('process');

const myargs = process.argv.slice(2);
const myurl = myargs[0];

request(myurl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
