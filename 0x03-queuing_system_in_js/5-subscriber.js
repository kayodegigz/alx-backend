import { createClient } from "redis";

//redis client
const client = createClient();

//handles connection error
client.on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`);
});

//connects to redis server
client.on('connect', () => {
    console.log(`Redis client connected to the server`);
});

//subscribe to a channel
client.subscribe('holberton school channel');

//listen formessageonchannel and print message when recieved
client.on('message', (channel, message) => {
    console.log(`${message}`);
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.end(true);
    }
});