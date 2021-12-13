#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const array = [];
  for (let i = 2; i < process.argv.length; i++) {
    array.push(parseInt(process.argv[i], 10));
  }
  array.sort(function (a, b) { return a - b; });
  console.log(array[array.length - 2]);
}
