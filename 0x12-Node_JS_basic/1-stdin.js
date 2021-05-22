console.log('Welcome to Holberton School, what is your name?');
process.stdin.once('data', (chunk) => {
  const name = chunk.toString().trim();
  if (name) {
    console.log(`Your name is: ${name}`);
  }
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
