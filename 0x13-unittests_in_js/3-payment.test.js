const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const utl = require('./utils.js');
const chai = require('chai');

describe('smoke test', function () {
  const spies = sinon.spy(utl, 'calculateNumber');
  it('checks output', function () {
    sendPaymentRequestToApi(100, 20);
    chai.expect(spies.calledOnce).to.be.true;
    chai.expect(spies.calledWith('SUM', 100, 20)).to.be.true;
    spies.restore();
  });
});
