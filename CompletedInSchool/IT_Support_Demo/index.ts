import { ask } from "./userPrompt_Wrapper/mod";
import {getDevice, DeviceTypes, Device} from './functions/getDevice'
import { DEVICE_IS_WET } from "./solutions";

async function run() {
    // Device data
    const deviceData = await getDevice().catch(e => {
        console.log(e);
        process.exit(1);
    });

    if(!deviceData) {
        throw new Error("NO DEVICE SPECIFIED");
    }

    const isWet = await ask<string>("Is the phone wet? (no)", "no").catch(e => {
        throw new Error(e);
    });

    if(isWet && (isWet.toLowerCase() == "true" || isWet.toLowerCase() == "yes")) {
        console.log(DEVICE_IS_WET);
        process.exit(0);
    }
}

run();