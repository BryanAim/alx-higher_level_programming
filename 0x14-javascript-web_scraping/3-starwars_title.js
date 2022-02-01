#!/usr/bin/node
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.error(err); }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
