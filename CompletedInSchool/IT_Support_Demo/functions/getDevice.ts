import { ask } from "../userPrompt_Wrapper/mod";

export function getDevice(): Promise<Device | null> {
    return new Promise(async (resolve, reject) => {
        const deviceType = await ask<String>('What device type are you having issues on (Phone, Laptop)');
        if(!deviceType) {
            reject('A device type is required.');
            return;
        }

        if(deviceType.toLowerCase() == "phone" || deviceType.toLowerCase() == "mobile phone") {
            // Get device model and make
            const deviceMaker = await ask<string>('Who made your device');
            if(!deviceMaker) {
                return reject('I need to know the device maker to help');
            }

            const deviceModel = await ask<string>('What model device is it?');
            if(!deviceModel) {
                return reject('I need to know the device model to help');
            }

            const osVersion = await ask<string>('What OS version are you on (if known)');
            if(osVersion) {
                const phone: Phone = {
                    model: deviceModel,
                    maker: deviceMaker,
                    OSVer: osVersion,
                    type: 'PHONE'
                }

                return resolve(phone);
            }

            const phone: Phone = {
                model: deviceModel,
                maker: deviceMaker,
                OSVer: 'UNKNOWN',
                type: 'PHONE'
            }
            return resolve(phone);
        }

        if(deviceType.toLowerCase() == "laptop") {
            const deviceMaker = await ask<string>('Who made your device');
            if(!deviceMaker) {
                return reject('I need to know the device maker to help');
            }

            const deviceModel = await ask<string>('What model device is it?');
            if(!deviceModel) {
                return reject('I need to know the device model to help');
            }

            const osVersion = await ask<string>('What OS version are you on (if known)');
            if(osVersion) {
                const laptop: Laptop = {
                    model: deviceModel,
                    maker: deviceMaker,
                    OSVer: osVersion,
                    type: 'LAPTOP'
                }

                return resolve(laptop);
            }

            const laptop: Laptop = {
                model: deviceModel,
                maker: deviceMaker,
                OSVer: 'UNKNOWN',
                type: 'LAPTOP'
            }

            return resolve(laptop);
        }

        return reject('Unknown device type');
    })
}

interface D {
    model: string;
    maker: string;
    OSVer: string | 'UNKNOWN';
}

export interface Phone extends D {
    type: 'PHONE';
}

export interface Laptop extends D {
    type: 'LAPTOP';
}

export type Device = Phone | Laptop;