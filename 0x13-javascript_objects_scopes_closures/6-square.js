#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i = 0;

    if (c) {
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
    else {
      c = 'X';
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
