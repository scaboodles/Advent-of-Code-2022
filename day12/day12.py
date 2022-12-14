#!/usr/bin/env python3

def start():
    input = open("./testInput.txt", "r")
    lines = input.read().splitlines()
    findPath(lines)

def findPath(lines):
    grid = gridify(lines)
    startPos, endPos = findStartEnd(grid)
    bestPath = recursivePathSearch(startPos, endPos, grid, [], None)
    print(bestPath)

def recursivePathSearch(curr, target, grid, previous, shortest):
    previous.append(curr)
    possibleMoves = [] 
    nearbyPoints = getSurrounding(curr, grid)

    for point in nearbyPoints:
        if comparePoints(grid, curr, point) and not point in previous:
            possibleMoves.append(point)

    print("current point: " + str(curr) + " with value : " + grid[curr[0]][curr[1]])
    print("possible moves: " + str(possibleMoves))
    
    if len(possibleMoves) > 0:
        if target in possibleMoves:
            print("reached end! with " + str(len(previous) -1 ) + " steps")
            if shortest:
                if shortest <= len(previous) -1:
                    return shortest
            return len(previous) -1
        else:
            for move in possibleMoves:
                new = recursivePathSearch(move, target, grid, previous, shortest)
                if new:
                    shortest = new
    print("~~~~~~~~~~~~~~")

def getSurrounding(curr, grid):
    points=[]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(curr[0] + i >= 0 and curr[0] + i < len(grid)) and (curr[1] + j >= 0 and curr[1] + j < len(grid[0])):
                if not (i == 0 and j == 0):
                    if i == 0 or j == 0:
                        points.append([curr[0] + i,curr[1] + j])
    return points

def findStartEnd(grid):
    stPos = None
    endPos = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                stPos = [i, j]
            elif grid[i][j] == 'E':
                endPos = [i, j]
            if(stPos and endPos):
                return stPos, endPos 
    return stPos, endPos 

def comparePoints(grid, a, b):
    p1 = grid[a[0]][a[1]]
    p2 = grid[b[0]][b[1]]
    if p1 == 'S':
        p1 = 'a'
    elif p1 == 'E':
        p1 = 'z'

    if p2 == 'S':
        p2 = 'a'
    elif p2 == 'E':
        p2 = 'z'

    if abs(ord(p1) - ord(p2)) <= 1:
        return True
    return False

def gridify(lines):
    newGrid = []
    for line in lines:
        newGrid.append(list(line))
    return newGrid

start()