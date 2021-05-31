var redis = require('redis');
var client = redis.createClient();

const name = 'HolbertonSchools';
async function main() {
  const shamu = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  try {
    for (const prop in shamu) {
      client.hset(name, prop, shamu[prop], redis.print);
    }
  } catch (error) {
    console.error(error);
  } finally {
    const str = await hgetall(name);
    console.log(str);
  }
}
main();
