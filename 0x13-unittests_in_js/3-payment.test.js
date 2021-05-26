const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const utl = require('./utils.js');
const chai = require('chai');

describe('smoke test', function () {
  it('checks output', function () {
    const spies = sinon.spy(utl, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    chai.expect(spies.calledWith('SUM', 100, 20)).to.equal(true);
    spies.restore();
  });
});
