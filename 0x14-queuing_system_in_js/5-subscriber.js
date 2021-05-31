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

client.subscribe('holberton school channel');

client.on('message', function (channel, message) {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    process.exit();
  }
});
