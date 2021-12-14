#!/usr/bin/node
exports.converter = function (base) {
  return function converter (number) {
    return number.toString(base);
  };
};
