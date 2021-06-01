import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

var queue = kue.createQueue();

var job;
for (job in jobs) {
  const newjob = queue
    .create('push_notification_code', job)
    .save(function (err) {
      if (!err) console.log(`Notification job created: ${newjob.id}`);
    });
  newjob.on('complete', function () {
    console.log(`Notification job ${newjob.id} completed`);
  });
  newjob.on('failed', function (error) {
    console.log(`Notification job ${newjob.id} failed: ${error}`);
  });
  newjob.on('progress', function (progress) {
    console.log(`Notification job ${newjob.id} ${progress}% complete`);
  });
}
