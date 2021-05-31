var redis = require('redis');
var client = redis.createClient();
var { promisify } = require('util');
var getting = promisify(client.get).bind(client);

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

async function displaySchoolValue(schoolName) {
  console.log(`${await getting(schoolName)}`);
}

(async function () {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
