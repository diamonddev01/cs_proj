type lightState = "Red" | "RedYellow" | "Green" | "Yellow";

class Light {
    private saveState: lightState;
    public group: number;

    constructor(saveState: lightState, groupNumber: number) {
        this.saveState = saveState;
        this.group = groupNumber;
    }

    get state(): lightState {
        return this.saveState;
    }

    set state(state: lightState) {
        this.saveState = state;
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
}

class Manager {
    private lights: Manager2DArray;
    private groups: Group[];
    private litGroupIndex: number;

    constructor(groups: Group[]) {
        this.groups = groups;
        this.lights = [];
        this.litGroupIndex = 0;

        for(let i = 0; i < this.groups.length; i++) {
            const group = groups[i];
            const lights: Light[] = [];
            for(let l = 0; l < group.light_count; l++) {
                lights.push(new Light("Red", i));
            }

            this.lights.push(lights);
        }

        this.tick(this);
    }

    public get states() {
        return this.lights;
    }

    private set states(lights: Manager2DArray) {
        this.lights = lights;
    }
    
    private tick(self: Manager) {
        const groupdId = this.litGroupIndex;
        const light_0 = this.lights[groupdId][0].state;

        switch(light_0) {
            case "Red":
                this.changeGroupState(groupdId, "RedYellow");
                setTimeout((tickfn: typeof this.tick, self: Manager) => {
                    tickfn(self)
                }, this.groups[groupdId].yellow_time * 1000, self.tick, self);
                break;
            case "RedYellow":
                this.changeGroupState(groupdId, "Green");
                setTimeout((tickfn: typeof this.tick, self: Manager) => {
                    tickfn(self)
                }, this.groups[groupdId].green_time * 1000, self.tick, self);
                break;
            case "Green":
                this.changeGroupState(groupdId, "Yellow");
                setTimeout((tickfn: typeof this.tick) => {
                    tickfn()
                }, this.groups[groupdId].yellow_time * 1000, this.tick);
                break;
            case "Yellow":
                this.changeGroupState(groupdId, "Red");
                this.litGroupIndex++;
                if(this.litGroupIndex >= this.groups.length) this.litGroupIndex = 0;
                this.tick();
                break;
        }
    }

    private changeGroupState(group_id: number, state: lightState) {
        if(group_id > this.groups.length - 1) return;
        for (const light of this.lights[group_id]) {
            light.state = state;
        }
    }

    public get getIndexState(): number {
        return this.litGroupIndex;
    }
}

const m = new Manager([{
    light_count: 3,
    green_time: 3,
    yellow_time: 1
},
{
    light_count: 3,
    green_time: 3,
    yellow_time: 1
}
]);

setInterval(() => {
    console.log(m.states);
    console.log(m.getIndexState)
}, 500);