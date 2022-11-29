import * as readLine from 'readline';

// Create RL interface
const rl = readLine.createInterface({
    input: process.stdin,
    output: process.stdout
});

export async function ask<T>(question: string, def?: any): Promise<T | null> {
    return new Promise((resolve) => {
        rl.question(question + ' ', (d: string) => {
            const data = d ??= def ??= null;
            resolve(data as T);
        });
    });
}