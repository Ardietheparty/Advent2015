ini = 29000000
nini = int ( ini / 10)
houses = [0]*ini
test = True
r=0
temp = False
for i in range(1, nini):
    for j in range(i, nini, i):
        houses[j]+=i * 10

for i in range(nini):
    if houses[i] >= ini:
        print(i)
        break
house = [0]*51
while test:
    elf = 1
    for j in range(1, nini):
        for i in range(1, 51, j):
            house[i] += j * 11
            if house[i] >= ini:
                #print(i)
                test = False
                break
    if test:
        break
for i in range(1, 51):
    if house[i] >= ini:
        print(i)
        break
