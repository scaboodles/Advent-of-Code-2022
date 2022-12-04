#!/usr/bin/env python3
def main():
    input = open("./input.txt", "r")
    pairs = splitPairs(input)
    indexPairs = splitIndexes(pairs)
    part2(indexPairs)

def part2(indexPairs):
    sum = checkLooseOverlap(indexPairs)
    print("Total partial overlaps: " + str(sum))

def checkLooseOverlap(indexPairs):
    sum = 0
    for pair in indexPairs:
        sum += checkBetween(pair) 
    return sum

def checkBetween(pair):
    p1 = makeInt(pair[0])
    p2 = makeInt(pair[1])
    if between(p1[0], p2) or between(p1[1], p2) or between(p2[0], p1) or between(p2[1], p1):
        print(str(p1) + " and " + str(p2) + " overlap")
        return 1

    print(str(p1) + " and " + str(p2) + " do not overlap")
    return 0

def makeInt(index):
    intPair = []
    intPair.append(int(index[0]))
    intPair.append(int(index[1]))
    return intPair

def p1(indexPairs):
    sum = checkAllOverlap(indexPairs)
    print("Total complete overlaps: " + str(sum))

def checkAllOverlap(indexes):
    sum = 0
    for pair in indexes:
        sum += pairOverlap(pair)
    return sum

def pairOverlap(pair):
    return 1 if contains(pair[0],pair[1]) or contains(pair[1],pair[0]) else 0

def contains(p1, p2):
    if int(p1[0]) <= int(p2[0]) and int(p1[1]) >= int(p2[1]):
        #print(str(p1) + " overlaps " + str(p2))
        return True

def between(num, pair):
    return num >= pair[0] and num <= pair[1]


def splitPairs(input):
    pairs = []
    for x in input:
        x = x.replace("\n", "")
        pair = x.split(",")
        pairs.append(pair)
    return pairs

def splitIndexes(pairs):
    indexPairs = []
    for pair in pairs:
        newIndex = []
        for index in pair:
            newIndex.append(index.split("-"))
        indexPairs.append(newIndex)
    return indexPairs




main()