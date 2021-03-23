#!/usr/bin/node

let myFuncCalls = -1;

exports.logMe = function (item) {
  myFuncCalls++;
  console.log(myFuncCalls + ': ' + item);
};
