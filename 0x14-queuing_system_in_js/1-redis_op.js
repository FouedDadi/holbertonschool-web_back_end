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

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, function (error, response) {
    redis.print(`Reply: ${response}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, function (error, response) {
    console.log(`${response}`);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
