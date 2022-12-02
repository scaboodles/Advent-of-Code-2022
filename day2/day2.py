#!/usr/bin/env python3
pointsMap = {"X" : 1, "Y" : 2, "Z" : 3}
throwMap = {"X" : "A", "Y" : "B", "Z" : "C"}

winTable = {"A":"Y" , "B" : "Z" , "C" : "X"}
drawTable = {"A" : "X", "B" : "Y", "C" : "Z"}
loseTable = {"A" : "Z", "B" : "X", "C":"Y"}

conditionTable = {"X" : loseTable, "Y" : drawTable, "Z" : winTable}

def main():
    input = open("./input.txt", "r")
    total = 0
    for x in input:
       txt = x.split() 
       score = compareThrows2(txt)
       total += score
    print("Total points: " + str(total))

def compareThrows2(round):
    points = 0
    if(round[1] == "X"):
        points += 0
    elif(round[1] == "Y"):
        points+=3
    else:
        points += 6
    myThrow = conditionTable[round[1]][round[0]]
    print(round[0], throwMap[myThrow], round[1], "|", "points for throw: ", pointsMap[myThrow], " points for condition: ", points)
    points += pointsMap[myThrow]
    return points

def compareThrows(round):
    points = 0
    points += pointsMap[round[1]]
    if(round[0] == throwMap[round[1]]):
        points += 3
    else:
        if(round[0] == "A"):
            if(round[1] == "Y"):
                points += 6 
            else:
                points += 0
        elif(round[0] == "B"):
            if(round[1] == "Z"):
                points += 6 
            else:
                points += 0
        elif(round[0] == "C"):
            if(round[1] == "X"):
                points += 6 
            else:
                points += 0
    return points

main()