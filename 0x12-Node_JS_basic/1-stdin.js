console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (chunk) => {
  const name = chunk.toString().trim();
  if (name) {
    console.log(`Your name is: ${name}`);
  }
  process.stdin.on('close', () => {
    console.log('This important software is now closing');
  });
});
