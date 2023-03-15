#!/usr/bin/node
let secondBiggest = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  secondBiggest = args[args.length - 2];
}
console.log(secondBiggest);
