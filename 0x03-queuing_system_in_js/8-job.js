const createPushNotificationsJob = (jobs, queue) => {
    // verify if jobs is an object
    if (!Array.isArray(jobs)) {
        throw Error('Jobs is not an array');
    }
    // creates the job with iterated job data
    jobs.forEach((data) => {
        let job = queue.create('push_notification_code_3', data).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${job.id}`);
            }
    });
    //job process to handle "complete" "failure" and "progress" of the jobs
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
}

module.exports = createPushNotificationsJob;