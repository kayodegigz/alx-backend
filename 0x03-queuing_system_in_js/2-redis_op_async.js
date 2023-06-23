import { createClient, print } from "redis";
import { promisify } from 'util';

const client = createClient();

client.on('error', err => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
    console.log(`Redis client connected to the server`);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
};


const get = promisify(client.get).bind(client);

async function displaySchoolValue() {
    const result = await get("schoolName").catch((error) => {
        if (error) {
            console.log(error);
            throw error;
        }
    });
    console.log(`${result}`);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');