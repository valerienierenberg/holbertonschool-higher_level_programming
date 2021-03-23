#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const count = list.reduce(function (n, val) {
    return n + (val === searchElement);
  }, 0);

  return (count);
};
