#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

request.get('https://swapi-api.hbtn.io/api/people/18/', function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
