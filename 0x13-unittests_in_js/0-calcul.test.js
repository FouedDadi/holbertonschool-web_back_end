const calculateNumber = require('./0-calcul.js');
const assert = require('assert');

describe('smoke test', function () {
  it('checks output and negative args', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    assert.strictEqual(calculateNumber(-2, 4), 2);
    assert.strictEqual(calculateNumber(-5, -10), -15);
  });
  it('check arguments', function () {
    assert.strictEqual(isNaN(calculateNumber(2)), true);
  });
});
