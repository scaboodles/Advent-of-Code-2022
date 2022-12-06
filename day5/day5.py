import re

def main():
    input = open("./input.txt", "r")
    crates = getCrates(input)
    part1(crates, input)

def part1(crates, input):
    atInstruct = False
    for x in input:
        if atInstruct:
            x = x.replace("\n", "")
            m = re.match(r"move (\d+) from (\d+) to (\d+)", x)
            assert m
            cnt, col_from, col_to = m.groups()
            cnt = int(cnt)
            col_from = int(col_from)
            col_to = int(col_to)
            col_from -= 1
            col_to -= 1
            crates = moveCrates(crates, cnt, col_from, col_to)
        if x == "\n":
            atInstruct = True
    printTops(crates) 

def printTops(crates):
    temp = ""
    for col in crates:
        if len(col) >= 1:
            temp += col[0]
    print(temp)

def moveCrates(crates, cnt, _from, _to):
    fromCol = crates[_from]
    toCol = crates[_to]
    fromCol, inTransit = removeCrate(fromCol, cnt) 
    toCol = placeCrates(toCol, inTransit)
    crates[_from] = fromCol
    crates[_to] = toCol
    return crates

def placeCrates(col, moving):
    newCol = moving
    for item in col:
        newCol.append(item)
    return newCol


def removeCrate(col, count):
    inTransit = []
    for i in range(count):
        inTransit.append(col.pop(0))
    #turned off for p2
    #inTransit.reverse()
    return col, inTransit


def getCrates(input):
    crates = []
    for x in input:
        if(" 1" in x):
            break
        line = x.replace("\n", "").replace("[", "").replace("]","")
        emptycount = 0
        newline = []
        justEmpty = False
        for char in list(line):
            if char == " ":
                if(not justEmpty):
                    emptycount += 1
                    if emptycount >= 3:
                        newline.append(" ")
                        emptycount = 0
                        justEmpty = True
                else:
                    justEmpty = False
            else:
                emptycount = 0
                newline.append(char)
        crates.append(newline)
    return sortCrates(crates)

def sortCrates(crates):
    sorted =[]
    for i in range(len(crates[0])):
        col = []
        for row in crates:
            if not row[i] == " ":
                col.append(row[i]) 
        sorted.append(col)
    return sorted

def printLines(input):
    for x in input:
        print(list(x))

main()