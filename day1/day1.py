#!/usr/bin/env python3


def main():
    calories = []
    input = open("input.txt", "r")
    num = 0
    for x in input:
        if(x == "\n"):
           calories.append(num)
           num = 0 
        else:
            num+=int(x)
    findTop3(calories)

def findTop(cal):
    print(str(max(cal)))

def findTop3(cal):
    total = 0
    for i in range(3):
        max = cal[0]
        index = 0
        for i in range(1,len(cal)):
            if cal[i] > max:
                max = cal[i]
                index = i
        total += max
        cal.pop(index)
    print(total)


main()
