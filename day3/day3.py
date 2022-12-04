def main():
    input = open("./input.txt")
    prob2(input)

def prob2(input):
    prioritySum = 0
    groupCounter = 0
    group = []
    for x in input:
        x = x.replace("\n","")
        if groupCounter < 3:
            group.append(x)
        else:
            prioritySum += findPriority(findGroupMatch(group))
            group = [x]
            groupCounter = 0
        groupCounter+=1
    
    prioritySum += findPriority(findGroupMatch(group))
    print(str(prioritySum))

def findGroupMatch(group):
    for i in range(len(group[0])):
        for j in range(len(group[1])):
            for k in range(len(group[2])):
                if group[0][i] == group[1][j]:
                    if group[1][j] == group[2][k]:
                        return group[0][i]

def prob1(input):
    prioritySum = 0
    for x in input:
        matchingChar = findMatch(x)
        prioritySum += findPriority(matchingChar)
    print(str(prioritySum)) 

def findPriority(char):
    if(char.islower()):
        return ord(char) - 96
    else:
        return ord(char) - 38

def findMatch(str):
    bag1, bag2 = splitItems(str)
    charMatch = ""
    for i in range(len(bag1)):
        for j in range(len(bag2)):
            if bag1[i] == bag2[j]:
                charMatch = bag1[i]
    return charMatch


def splitItems(str):
    str = str.replace("\n", "")

    str1 = str[0 : int(len(str)/2)]
    str2 = str[int(len(str)/2):]

    return str1, str2

main()