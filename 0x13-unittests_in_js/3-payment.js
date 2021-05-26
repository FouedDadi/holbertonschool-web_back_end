const Utils = require('./utils');
function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const call = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`total is: ${call}`);
}
module.exports = sendPaymentRequestToApi;
