#!/usr/bin/node
let nextMax = 0;
const args = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (args.length > 1) {
  args.sort();
  nextMax = args[args.length - 2]
  console.log(nextMax);
} else {
  console.log(nextMax);
}
