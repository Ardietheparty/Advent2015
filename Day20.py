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

