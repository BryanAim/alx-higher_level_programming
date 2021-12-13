#!/usr/bin/node
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10)));
