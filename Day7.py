def keyz(dic, str, num):
    if str in dic:
        dic[str] = num
    else:
        dic.update({str: num})

def AND(dic, str):
    str = str.split(' ')
    a = str[0]
    b = str[2]
    c = str[4]
    
def oper(str):
    operations = ["AND", "OR", "NOT", "RSHIFT", "LSHIFT"]
    if operations[0] in str:
        return 0
    elif operations[1] in str:
        return 1
    elif operations[2] in str:
        return 2
    elif operations[3] in str:
        return 3
    elif operations[4] in str:
        return 4
    elif operations[5] in str:
        return 5
with open('Day7in', 'r') as f:
    for line in f:
        hold = line.split(" ")
        print(hold)