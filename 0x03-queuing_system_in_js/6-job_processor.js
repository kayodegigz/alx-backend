//import create queue from kue
import { createQueue } from "kue";

// assign createQueue() to queue
const queue = createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending Notification to ${phoneNumber}, with message ${message}`);
};

queue.process('push_notification_code', function(job, done) {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});