#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  const loop = function (x) {
    if (x) {
      theFunction(x);
      loop(--x);
    }
  };
  loop(x);
};
