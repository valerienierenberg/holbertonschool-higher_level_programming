#!/usr/bin/node

const list = require('./100-data').list;

const map1 = list.map((i, val) => i * val);

console.log(list);
console.log(map1);
