const express = require('express');

const app = express();

app.get('/', (req, res) => {
  if (req.url === '/') res.send('Hello Holberton School!');
  if (req.url === '/students') {
    res.send('This is the list of our students\n');
  } // write a response to the client
});
app.listen(1245);
module.exports = app;
