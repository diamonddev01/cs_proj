# THIS SOLUTION NEEDS FIXING

DRAW_WIN = "draw"

#'''
#input format
#<TNAME> <SECONDS> <ENEMY_HITS>
#Each enemy hit reduces seconds by 3
#'''

v = []
for i in range(4):
    v.append(input(""))

BEST_TEAM = "A"
BEST_TIME = 999999
DRAW_ACTIVE = True

for item in v:
    data = item.split(" ")
    TEAM_NAME = data[0]
    TEAM_TIME = int(data[1])
    TEAM_HITS = int(data[2])
    removed_time = TEAM_HITS * 3
    final_time = TEAM_TIME - removed_time

    #print(f"{TEAM_NAME} FINAL SCORE {final_time}")

    if final_time < BEST_TIME:
        BEST_TIME = final_time
        BEST_TEAM = TEAM_NAME
        DRAW_ACTIVE = False
        #print("NEW TOP")
    if final_time == BEST_TIME and TEAM_NAME != BEST_TEAM:
        DRAW_ACTIVE = True
        #print("DRAW TOP")

if DRAW_ACTIVE:
    print(DRAW_WIN)
else:
    print(BEST_TEAM)