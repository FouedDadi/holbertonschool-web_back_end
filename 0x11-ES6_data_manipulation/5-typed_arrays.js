export default function createInt8TypedArray(length, position, value) {
  if (position >= length) throw new Error('Position outside range');
  const buff = new ArrayBuffer(length);
  const arr = new DataView(buff, 0);
  arr.setInt8(position, value);
  return arr;
}
