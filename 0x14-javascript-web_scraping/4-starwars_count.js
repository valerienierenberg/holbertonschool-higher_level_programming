#!/usr/bin/node

const request = require('request');

request.get('https://swapi-api.hbtn.io/api/people/18/', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
