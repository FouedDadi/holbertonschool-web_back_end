export default function appendToEachArrayValue(array, appendString) {
  const arr = [];
  for (let val of array) {
    arr.push(appendString + val);
  }
  return arr;
}
