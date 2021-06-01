import kue from 'kue';
const queue = kue.createQueue();

const bl = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (bl.includes(phoneNumber)) {
    return done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done();
  }
  queue.process('push_notification_code_2', 2, function (jb, done) {
    sendNotification(jb.phoneNumber, jb.message, jb, done);
  });
}
