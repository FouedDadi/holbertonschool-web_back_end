const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('smoke test', function () {
  it('checks output', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('check arguments', function () {
    assert.strictEqual(isNaN(calculateNumber(1)), true);
  });
});
