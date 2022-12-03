type lightState = "Red" | "RedYellow" | "Green" | "Yellow"; // All states a light is allowed to be in

class Light {
    private saveState: lightState; // The lights current state
    private group: number;

    /*
        saveState - The state the light will be assigned on construction
        groupNumber - The group that this light is tied to
    */
    constructor(saveState: lightState, groupNumber: number) {
        this.saveState = saveState; // Allocates the saveState
        this.group = groupNumber; // Allocates the group.
    }

    public get state(): lightState {
        return this.saveState; // Returns the light state to be used in a different calculation
    }

    public set state(state: lightState) {
        this.saveState = state; // Sets the light state from another claculation or by the manager.
    }

    public get groupNumber(): number {
        return this.group; // Used to make a public version of the private this.group prop.
    }
}

/*
this.lights[group_number][light_number]
*/
type Manager2DArray = Light[][]
interface Group {
    light_count: number;
    green_time: number; // seconds
    yellow_time: number; // seconds
    red_yellow_time: number; // seconds
}

// Operates the lights
class Manager {
    private lights: Manager2DArray;
    private groups: Group[];
    private litGroupIndex: number;

    constructor(groups: Group[]) { // Inits with an array of group items
        this.groups = groups; // sets the group items into this.groups
        this.lights = []; // Creates an array and allocates it so that lights can be placed in it later.
        this.litGroupIndex = 0; // Sets the index to be the first item of the arrays

        // Initialises all of the required lights
        for(let i = 0; i < this.groups.length; i++) {
            const group = groups[i];
            const lights: Light[] = [];
            for(let l = 0; l < group.light_count; l++) {
                lights.push(new Light("Red", i));
            }

            this.lights.push(lights);
        }

        // Makes one change to the light system so the first lights change state
        this.tick(this);
    }

    // Logging purposes and also used in other calculations
    public get states() {
        return this.lights;
    }

    // Made so that the states() is a GET,SET
    private set states(lights: Manager2DArray) {
        this.lights = lights;
    }
    
    // Moves the lights by one item over in the index of states
    // This uses "self" as the Manager because of setTimeout being odd
    private tick(self: Manager) {
        const groupdId = self.litGroupIndex;
        const light_0 = self.lights[groupdId][0].state;

        switch(light_0) {
            case "Red":
                self.changeGroupState(groupdId, "RedYellow");
                setTimeout((tickfn: typeof self.tick, self: Manager) => {
                    tickfn(self)
                }, self.groups[groupdId].red_yellow_time * 1000, self.tick, self);
                break;
            case "RedYellow":
                self.changeGroupState(groupdId, "Green");
                setTimeout((tickfn: typeof self.tick, self: Manager) => {
                    tickfn(self)
                }, self.groups[groupdId].green_time * 1000, self.tick, self);
                break;
            case "Green":
                self.changeGroupState(groupdId, "Yellow");
                setTimeout((tickfn: typeof self.tick, self: Manager) => {
                    tickfn(self)
                }, self.groups[groupdId].yellow_time * 1000, self.tick, self);
                break;
            case "Yellow":
                self.changeGroupState(groupdId, "Red");
                self.litGroupIndex++;
                if(self.litGroupIndex >= self.groups.length) self.litGroupIndex = 0;
                self.tick(self);
                break;
        }
    }

    // Changes the state of every light inside of the group
    /*
        group_id - The index that will be used
        state: the state to change them to
    */
    private changeGroupState(group_id: number, state: lightState) {
        if(group_id > this.groups.length - 1) return; // If it is an invalid index then return out;

        // sets the state of every light
        for (const light of this.lights[group_id]) {
            light.state = state;
        }
    }

    // Returns the current indexState for logging purposes
    public get getIndexState(): number {
        return this.litGroupIndex;
    }
}

// DEMO CODE
const m = new Manager([{
    light_count: 3,
    green_time: 3,
    yellow_time: 1,
    red_yellow_time: 1
},
{
    light_count: 3,
    green_time: 3,
    yellow_time: 1,
    red_yellow_time: 1
},
{
    light_count: 6,
    green_time: 7,
    yellow_time: 2,
    red_yellow_time: 1
}
]);

setInterval(() => {
    console.log(m.states);
}, 250);