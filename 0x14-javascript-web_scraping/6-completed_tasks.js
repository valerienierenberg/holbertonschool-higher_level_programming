#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const complete = {};
    const tasks = JSON.parse(body);
    let i = 0;
    for (i = 0; i < tasks.length; i++) {
      if (!(tasks[i].userId in complete)) {
        complete[tasks[i].userId] = 0;
      }
      if (tasks[i].completed) {
        complete[tasks[i].userId] += 1;
      }
      if (complete[tasks[i].userId] === 0) {
        delete complete[tasks[i].userId];
      }
    }
    console.log(complete);
  }
});
