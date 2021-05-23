const http = require('http');

// create a server object:
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' }); // HTTP header with content type
  if (req.url === '/') res.write('Hello Holberton School!');
  if (req.url === '/students') {
    res.write('This is the list of our students\n');
  } // write a response to the client
  res.end(); // end the response
});
app.listen(1245);
module.exports = app;
