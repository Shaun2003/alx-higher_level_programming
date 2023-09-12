#!/usr/bin/node
// function which returns number of occurrences in list

const originalList = require('./100-data').list;
console.log(originalList);
const mappedList = originalList.map (function (e, index) {
  return (e * index);
});
console.log(mappedList);
