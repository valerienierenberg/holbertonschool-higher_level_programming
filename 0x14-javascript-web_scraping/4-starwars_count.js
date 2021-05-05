#!/usr/bin/node

const request = require('request');

const myargs = process.argv.slice(2);
const myurl = myargs[0];

request.get(myurl, function (err, body) {
  if (err) {
    console.log(err);
  } else {
    let myresults = console.log(JSON.parse(body).results);
    // loop through myresults to find characters (a list) -- nested loop
  }
});

// .results
