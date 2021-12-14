#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurr = 0;
  for (let count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      ocurr = ocurr + 1;
    }
  }
  return ocurr;
};
