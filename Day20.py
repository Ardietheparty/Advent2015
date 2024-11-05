ini = 2900000
houses = [0]*ini
test = True
r=0
for i in range(1, ini):
    for j in range(i, ini, i):
        houses[j]+=j

for i in range(ini):
    if houses[i] == ini:
        print(i)
        break