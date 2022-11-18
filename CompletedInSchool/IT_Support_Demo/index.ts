import { ask } from "./userPrompt_Wrapper/mod";
import {getDevice} from './functions/getDevice'

async function run() {
    // Device data
    const deviceData = getDevice();

    deviceData.catch(e => {
        console.log(e);
        process.exit(1);
    }).then(data => {
        console.log(data);
    })
}

run();