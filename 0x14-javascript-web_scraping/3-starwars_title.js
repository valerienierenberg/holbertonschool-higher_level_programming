#!/usr/bin/node

const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2] + '/', function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCose === 200) {
    console.log(JSON.parse(body).title);
  }
});
