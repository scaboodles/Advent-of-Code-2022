#!/usr/bin/env python3
import copy
def main():
    file = open("input.txt", "r")
    countTrees(file)

def countTrees(file):
    lines = file.read().splitlines()
    visibleTreeGrid = constructGrid(lines)
    visibleTreeGrid = checkAllDirections(visibleTreeGrid, lines)
    visibleTrees = seeTrees(visibleTreeGrid)
    #print(visibleTrees) <- answer for p1
    treeValueGrid = valueGrid(lines)
    bestTreeVal = findBestTree(treeValueGrid)
    print(bestTreeVal)

def findBestTree(grid):
    highestVis = 0
    y,x = 0,0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            treeVis = calculateVis(i,j,grid)
            if treeVis > highestVis:
                highestVis = treeVis
                y,x = i,j
    return highestVis

def calculateVis(i, j, grid):
    rightVis = calcRightVis(i,j,grid)
    leftVis = calcLeftVis(i,j,grid)
    topVis = calcTopVis(i,j,grid)
    botVis = calcBotVis(i,j,grid)
    return botVis*topVis*rightVis*leftVis

def calcRightVis(i,j,grid):
    vis = 1
    height = grid[i][j]
    for x in range(len(grid[i]) - j - 1):
        index = j+x+1
        if grid[i][index] < height:
            if index < len(grid[i])-1:
                vis+=1
        else:
            return vis
    return vis

def calcLeftVis(i,j,grid):
    vis = 1
    height = grid[i][j]
    for x in range(j):
        index = j-x-1
        if grid[i][index] < height:
            if index > 0:
                vis+=1
        else:
            return vis
    return vis 

def calcTopVis(i,j,grid):
    vis = 1
    height = grid[i][j]
    for y in range(i):
        index = i-y-1
        if grid[index][j] < height:
            if index > 0:
                vis+=1
        else:
            return vis 
    return vis 

def calcBotVis(i,j,grid):
    vis = 1
    height = grid[i][j]
    for y in range(len(grid) - i - 1):
        index = y+i+1
        if grid[index][j] < height:
            if index < len(grid) - 1:
                vis+=1
        else:
            return vis 
    return vis 

def valueGrid(lines):
    trees = []
    for line in lines:
        row = []
        for char in list(line):
            row.append(int(char))
        trees.append(row)
    return trees


def seeTrees(grid):
    count = 0
    for row in grid:
        for tree in row:
            if tree:
                count+=1
    return count

def checkAllDirections(trees, lines):
    newTrees = trees
    newTrees = checkFromLeft(newTrees, lines)
    newTrees = checkFromTop(newTrees, lines)
    newTrees = checkFromBottom(newTrees, lines)
    newTrees = checkFromRight(newTrees, lines)
    return(newTrees)

def checkFromRight(grid, lines):
    newGrid = copy.deepcopy(grid)
    for i in range(len(lines)):
        row = lines[i]
        max = int(list(row)[len(row) - 1])
        for j in range(len(row)):
            index = (len(row) - 1) - j
            char = list(row)[index]
            digit = int(char)
            if digit > max:
                max = digit
                newGrid[i][index] = True
    return newGrid

def checkFromBottom(grid, lines):
    newGrid = copy.deepcopy(grid)
    for i in range(len(lines[0])):
        max = int(list(lines[len(lines) - 1])[i])
        for j in range(len(lines)):
            index = (len(lines) - 1) - j
            char = list(lines[index])[i]
            digit = int(char)
            if digit > max:
                max = digit
                newGrid[index][i] = True
    return newGrid

def checkFromTop(grid, lines):
    newGrid = copy.deepcopy(grid)
    for i in range(len(lines[0])):
        max = int(list(lines[0])[i])
        for j in range(len(lines)):
            char = list(lines[j])[i]
            digit = int(char)
            if digit > max:
                max = digit
                newGrid[j][i] = True
    return newGrid

def checkFromLeft(grid, lines):
    newGrid = copy.deepcopy(grid)
    for i in range(len(lines)):
        row = lines[i]
        max = int(list(row)[0])
        for j in range(len(row)):
            char = list(row)[j]
            digit = int(char)
            if digit > max:
                max = digit
                newGrid[i][j] = True
    return newGrid

def constructGrid(lines):
    width = len(lines[0])
    trees = []
    for line in lines:
        add = [False] * width
        trees.append(add)
    return outerVisible(trees)

def outerVisible(trees):
    newTrees = copy.deepcopy(trees)
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if i == 0 or i == len(trees) - 1:
                newTrees[i][j] = True
            if j == 0 or j == len(trees[i]) - 1:
                newTrees[i][j] = True
    return newTrees

def prettyPrintGrid(grid):
    for row in grid:
        strBuf = ""
        for tree in row:
            if tree:
                strBuf+="T"
            else:
                strBuf+=" "
        print(strBuf)

def prettyPrintValueGrid(grid):
    for row in grid:
        strBuf = ""
        for tree in row:
            strBuf += str(tree)
        print(strBuf)


main()