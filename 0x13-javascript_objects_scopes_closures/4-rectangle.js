#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempW = this.width;
    const tempH = this.height;

    this.width = tempH;
    this.height = tempW;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
