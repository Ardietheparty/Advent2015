import numbers


def surfaceArea(a, b, c):
    #print(a, b, c)
    ab = a*b
    ac = a*c
    bc = b*c
    #(ab, ac, bc)
    total = 2*(ab + ac + bc)
    if ab <= ac and ab <= bc:
        total += ab
        #print("ab")

    elif ac <= bc and ac <= ab:
        total += ac
        #print("ac")
    else:
        total += bc
        #print("bc",bc)
    return total

def perimiter(a, b, c):
    numbers = [0, 0, 0]
    numbers[0] = a
    numbers[1] = b
    numbers[2] = c
    numbers.sort()
    return numbers[0]+numbers[0]+numbers[1]+numbers[1] + (a*b*c)
allofit = 0
with open('day2in.txt', 'r') as f:
    for line in f:
        line = line.replace('\n','')
        hold = line.split('x')
        allofit += surfaceArea(int(hold[0]), int(hold[1]), int(hold[2]))
print(allofit)
allofit = 0
with open('day2in.txt', 'r') as f:
    for line in f:
        line = line.replace('\n','')
        hold = line.split('x')
        allofit += perimiter(int(hold[0]), int(hold[1]), int(hold[2]))

print(allofit)