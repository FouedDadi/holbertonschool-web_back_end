import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  var body;
  var firstName;
  var lastName;
  return uploadPhoto()
    .then((dt) => {
      body = dt.body;
      createUser()
        .then((dt) => {
          firstName = dt.firstName;
          lastName = dt.lastName;
          console.log(`${body} ${firstName} ${lastName}`);
        })
        .catch(() => console.log('Signup system offline'));
    })
    .catch(() => console.log('Signup system offline'));
}
