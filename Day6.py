###DID IN GO
from idlelib.replace import replace
import os
dimm = 1000
grid = [[0]*dimm]*dimm
total = 0
tmp = 0
a=0
with open('Day6in', 'r') as f:
    for line in f:
        if "turn on" in line:
            line = line.replace("turn on ", "")
            line = line.replace(" through", ",")
            line = line.replace('\n', "")
            hold = line.split(",")
            xi = int(hold[0])
            yi = int(hold[1])
            xf = int(hold[2])
            yf = int(hold[3])
            #print(xi, yi, xf, yf)
            #print((xf-xi) * (yf-yi))

            for x in range(xi, xf+1):
                for y in range(yi, yf+1):
                    grid[x][y] = 1

        if "turn off" in line:
            line = line.replace("turn off ", "")
            line = line.replace(" through", ",")
            line = line.replace('\n', "")
            hold = line.split(",")
            xi = int(hold[0])
            yi = int(hold[1])
            xf = int(hold[2])
            yf = int(hold[3])

            for x in range(xi, xf+1):
                for y in range(yi, yf+1):
                    grid[x][y] = 0
                    #print(grid[x][y])


        if "toggle" in line:
            line = line.replace("toggle", "")
            line = line.replace(" through", ",")
            line = line.replace('\n', "")
            hold = line.split(",")
            xi = int(hold[0])
            yi = int(hold[1])
            xf = int(hold[2])
            yf = int(hold[3])
            for x in range(xi, xf+1):
                for y in range(yi, yf+1):
                    #print(grid[x][y])
                    a+=1
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                    if grid[x][y] == 0:
                        grid[x][y] = 1
                    #print(grid[x][y])
                    #os.system('pause')

total = 0
ts = 0
#print(tmp)ts

for x in range(dimm):
    for y in range(dimm):
        total += grid[x][y]
        ts+=1
print(total)

############DID IN GO