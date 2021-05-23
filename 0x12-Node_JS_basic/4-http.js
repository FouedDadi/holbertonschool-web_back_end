const http = require('http');

// create a server object:
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' }); // HTTP header with content type
  res.write('Hello Holberton School!'); // write a response to the client
  res.end(); // end the response
});
app.listen(1245);
module.exports = app;
