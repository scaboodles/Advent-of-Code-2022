import re
import copy

def main():
    file = open("./input.txt", "r")
    fileTree = constructTree(file)
    sum, tRecount = sumFiles(fileTree, 100000)
#    V answer to p1 V
#    print(sum)
#    ----------
    freeSpace = 70000000 - tRecount["/"]["Files sum"]
    spaceNeeded = 30000000 - freeSpace
    print(findSmallestFit(tRecount, spaceNeeded))


def findSmallestFit(tree, fit):
    smallest = anotherRecursiveSearch(tree, tree["/"]["Files sum"], fit)
    return smallest
    
def anotherRecursiveSearch(tree, smol, fit):
    for key,value in tree.items():
        if key == "Files sum":
            if value < smol and value >= fit:
                smol = value
        else:
            smol = anotherRecursiveSearch(tree[key], smol, fit)
    return smol

def totalSumTree(tree):
    newTree = copy.deepcopy(tree) 
    newTree["Files sum"] = recursiveTotalSum(newTree)
    return newTree

def recursiveTotalSum(tree):
    thisSum = 0
    for key,value in tree.items():
        if key == "Files sum":
            thisSum += value
        else:
            thisSum += recursiveTotalSum(tree[key])
    tree["Files sum"] = thisSum
    return thisSum


def sumFiles(tree, maxSize):
    doubledUp = totalSumTree(tree)
    sum = recursiveSearchDict(0, doubledUp, maxSize)
    return sum, doubledUp

def recursiveSearchDict(sum, tree, maxSize):
    for key,value in tree.items():
        if key == "Files sum":
            if value <= maxSize:
                sum += value
        else:
            newsum = recursiveSearchDict(0, tree[key], maxSize)
            sum += newsum
    return sum

def constructTree(input):
    knownPaths = ["/"]
    tree = {"/" : {"Files sum" : 0}}
    currDir = "/"
    lines = input.read().splitlines()
    for x in lines:
        if "$" in x:
            cmd = x[2:4]
            if cmd == "cd":
                cdDir = x[5:]
                if cdDir == "..":
                    currDir = dotdot(currDir)
                else:
                    if not cdDir == "/":
                        if currDir + cdDir in knownPaths :
                            currDir += cdDir + "/" 
                        else:
                            getNestedDir(currDir, tree)[cdDir] = {}
                            currDir += cdDir + "/"
                            knownPaths.append(currDir)
                            getNestedDir(currDir, tree)["Files sum"] = 0
        else:
            getNestedDir(currDir, tree)["Files sum"] += getSize(x)
    return tree

def getSize(line):
    m = re.match(r"(\d+) (\S+)", line)
    if m:
        size, name = m.groups()
        return int(size)
    return 0

def dotdot(path):
    nest = path.split("/")
    length = len(nest)
    i = 0
    while i < length:
        if nest[i] == "":
            nest.pop(i)
            length -= 1
        i+=1
    nest.pop(len(nest)-1)
    newPath = "/".join(nest)
    newPath += "/"
    return newPath

def getNestedDir(path, tree):
    nest = path.split("/")
    acessed = tree["/"]
    for dir in nest:
        if not dir == "":
            acessed = acessed[dir]
    return acessed

main()