const request = require('request');
const chai = require('chai');

describe('testing status code and result', function () {
  it('200 code test and body test', function (done) {
    const info = { url: 'http://localhost:7865', method: 'GET' };
    request(info, function (error, response, bd) {
      chai.expect(response.statusCode).to.equal(200);
      chai.expect(bd).to.equal('Welcome to the payment system');
      done();
      if (error) console.log('eroor');
    });
  });
});
