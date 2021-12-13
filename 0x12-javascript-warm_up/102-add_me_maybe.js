#!/usr/bin/node
let nb;
exports.addMeMaybe = function (number, theFunction) {
  nb = number + 1;
  theFunction(nb);
};
