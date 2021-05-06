#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) throw err;
  if (res.StatusCode === 200) {
    const complete = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in complete) { complete[task.userId] += 1; } else { complete[task.userId] = 1; }
      }
    }
    console.log(complete);
  } else {
    console.log('An error occured.');
  }
});
