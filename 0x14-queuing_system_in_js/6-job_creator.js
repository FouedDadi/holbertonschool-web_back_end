import kue from 'kue';
var queue = kue.createQueue();

var dt = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};
var jb = queue.create('push_notification_code', dt).save(function (Error) {
  if (!Error) console.log(`Notification job created: ${jb.id}`);
});

jb.on('complete', function () {
  console.log('Notification job completed');
});
jb.on('failed', function () {
  console.log('Notification job failed');
});
