const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment.js');
const utl = require('./utils');
const chai = require('chai');

describe('smoke test', function () {
  var con;
  beforeEach(function () {
    con = sinon.spy(console, 'log');
  });
  afterEach(function () {
    con.restore();
  });
  it('checks output and number of calls', function () {
    const api = sendPaymentRequestToApi(100, 20);
    chai.expect(con.calledOnce).to.equal(true);
    chai.expect(con.calledWith('The total is: 120')).to.equal(true);
  });
  it('checks output and number of calls', function () {
    const api = sendPaymentRequestToApi(10, 10);
    chai.expect(con.calledOnce).to.equal(true);
    chai.expect(con.calledWith('The total is: 20')).to.equal(true);
  });
});
