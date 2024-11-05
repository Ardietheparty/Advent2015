import os
from platform import system


def testa(str):
    nums = 0
    for char in str:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            nums += 1
        if nums == 3:
            #print("1")
            return True
    return False

def testb(str):
    for i in range(len(str)-1):
        if str[i] == str[i+1]:
            return True
    return False

def testc(str):
    for i in range(len(str)-1):
        temp = str[i]+str[i+1]
        if temp == "ab" or temp == "cd" or temp == "pq" or temp == "xy":
            print(str[i], str[i+1])
            return False
    return True
numofstrings = 0
with open('Day5in', 'r') as f:
    for line in f:
        if testa(line) and testb(line) and testc(line):
            numofstrings += 1




print(numofstrings)