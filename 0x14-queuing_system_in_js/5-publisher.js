var redis = require('redis');
var client = redis.createClient();

client
  .on('connect', function () {
    console.log(`Redis client connected to the server`);
  })
  .on('error', function (error) {
    if (error)
      console.log(`Redis client not connected to the server: ${error}`);
  });

function publishMessage(message, time) {
  setTimeout(function () {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
