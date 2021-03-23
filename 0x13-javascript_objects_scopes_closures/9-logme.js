#!/usr/bin/node

var myFuncCalls = -1;

exports.logMe = function (item) {
  myFuncCalls++;
  console.log(myFuncCalls + ': ' + item);
};
