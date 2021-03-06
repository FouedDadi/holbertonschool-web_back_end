export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw new TypeError('name must be a string');
    if (typeof length !== 'number') throw new TypeError('Length must be a number');
    if (!Array.isArray(students)) throw new TypeError('students must be an array');
    for (const std of students) {
      if (typeof std !== 'string') throw new TypeError('std must be a string');
    }
    this._name = name;
    this._length = length;
    this._students = students;
  }

  set name(Name) {
    if (typeof Name !== 'string') throw new TypeError('Name must be a string');
    this._name = Name;
  }

  set length(Length) {
    if (typeof Length !== 'number') throw new TypeError('Length must be a number');
    this._length = Length;
  }

  set students(Students) {
    if (!Array.isArray(Students)) throw new TypeError('Stduents must be an array');
    for (const std of Students) {
      if (typeof std !== 'string') throw new TypeError('std must be a string');
    }
    this._students = Students;
  }

  get name() {
    return this._name;
  }

  get length() {
    return this._length;
  }

  get students() {
    return this._students;
  }
}
