//import create queue from kue
import { createQueue } from "kue";

// assign createQueue() to queue
const queue = createQueue();

// object for job data
const data = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

//create a queue named push notification and saves it with save()
const job = queue.create('push_notification_code', data).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
});

// checks if the job is complete or the job failed
job.on('complete', () => {
    console.log(`Notification job completed`);
}).on('failed', () => {
    console.log(`Notification job failed`);
});