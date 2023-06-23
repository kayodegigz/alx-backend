//import create queue from kue
import { createQueue } from "kue";

// assign createQueue() to queue
const queue = createQueue();


const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

jobs.forEach((data) => {
    // creates ajob queue with the iterated data
    let job = queue.create('push_notification_code_2', data).save((err) => {
        if (!err) {
            console.log(`Notification job created: ${job.id}`);
        }
    });
    
    // checks if the job is complete or the job failed
    job.on('complete', () => {
        console.log(`Notification job #${job.id} completed`);
    }).on('failed', (error) => {
        if (error) {
            console.log(`Notification job ${job.id} failed: ${error}`);
        }
    }).on('progress', (progress) => {
        console.log(`Notification job #${job.id} ${progress}% complete`);
    });
});