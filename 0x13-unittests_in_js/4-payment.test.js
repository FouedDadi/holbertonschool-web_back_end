const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const utl = require('./utils');
const chai = require('chai');

describe('smoke test', function () {
  it('checks output', function () {
    const con = sinon.spy(console, 'log');
    const stb = sinon.stub(utl, 'calculateNumber').returns(10);
    const api = sendPaymentRequestToApi(100, 20);
    chai.expect(con.calledWith('The total is: 10')).to.equal(true);
    chai.expect(stb.calledWith('SUM', 100, 20)).to.equal(true);
    con.restore();
    stb.restore();
  });
});
