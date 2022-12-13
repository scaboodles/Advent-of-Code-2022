#!/usr/bin/env python3

import math
import regex as re
import operator

ops = {"+":operator.add, "*":operator.mul}

class Monkey:
    activity = 0
    def __init__(self, id, startingItems, operation, test, trueFalse):
        self.id = id
        self.heldItems = startingItems
        self.operation, self.num = getOps(operation)
        self.test = test
        self.trueFalse = trueFalse

    def round(self, monkeys, superMod):
        if len(self.heldItems) > 0:
            for i in range(len(self.heldItems)):
                self.heldItems[i] = operate(self.heldItems[i], self.operation, self.num)
                self.activity += 1
                self.heldItems[i] = self.heldItems[i] % superMod
                action = decide(self.heldItems[i], self.test)
                throw(self.trueFalse[action], self.heldItems[i], monkeys)
            self.heldItems = []

    def printMonkey(self):
        print("id: " + str(self.id))
        print("heldItems: " + str(self.heldItems))
        print("operation: " + str(self.operation))
        print("test: " + str(self.test))
        print("t/f: " + str(self.trueFalse))

    def catch(self, item):
        self.heldItems.append(item)
    
    def getActivity(self):
        return self.activity

    def getTest(self):
        m = re.match(r"divisible by (\d+)", self.test)
        assert m
        testNum = int(m.groups()[0])
        return testNum

def throw(action, item, monkeys):
    m = re.match(r"throw to monkey (\d+)", action)
    assert m
    recipient = int(m.groups()[0])
    monkeys[recipient].catch(item)

def decide(item, test):
    m = re.match(r"divisible by (\d+)", test)
    assert m
    testNum = int(m.groups()[0])
    if(item%testNum == 0):
        return 0
    return 1

def operate(item, operator, num):
    if num == "old":
        num = item
    else:
        num = int(num)
    return int(ops[operator](item, num))

def getOps(operation):
    m = re.match(r"(.) (.+)", operation)
    oper, num = m.groups()
    return oper, num

def start():
    input = open("./input.txt", "r")
    lines = input.read().splitlines()
    input.close()
    monkeys = instantiateMonkeys(lines)
    activities = []
    for monkey in monkeys:
       activities.append(monkey.getActivity()) 
    activities.sort(reverse=True)
    monkeyBusiness = activities[0] * activities[1]
    print(monkeyBusiness)

def shenanigans(rounds, monkeys, supermod):
    for i in range(rounds):
        print("starting round " + str(i))
        for monkey in monkeys:
            monkey.round(monkeys, supermod)
    return monkeys

def instantiateMonkeys(lines):
    monkeys = []

    workingMonkeyId = 0
    currStartingItems = []
    currOperation = ""
    currTest = ""
    currTrueFalse = []
    for line in lines:
        m = re.match(r"Monkey (\d+):", line)
        if m:
            workingMonkeyId = m.groups()[0]
            continue

        m = re.match(r" +Starting items: (.+)", line)
        if m:
            items = m.groups()[0].split(", ")
            for num in items:
                currStartingItems.append(int(num))
            continue

        m = re.match(r" +Operation: new = old (.+)", line)
        if m:
            currOperation = m.groups()[0]
            continue

        m = re.match(r" +Test: (.+)", line)
        if m:
            currTest = m.groups()[0]
            continue

        m = re.match(r" +If true: (.+)", line)
        if m:
            currTrueFalse.append(m.groups()[0])
            continue

        m = re.match(r" +If false: (.+)", line)
        if m:
            currTrueFalse.append(m.groups()[0])
            continue
        
        monkeys.append(Monkey(workingMonkeyId, currStartingItems, currOperation, currTest, currTrueFalse))
        currStartingItems = []
        currTrueFalse = []

    monkeys.append(Monkey(workingMonkeyId, currStartingItems, currOperation, currTest, currTrueFalse))

    superMod = findSupermodulo(monkeys)

    return shenanigans(10000, monkeys, superMod)

def findSupermodulo(monkeys):
    superMod = 1
    for monkey in monkeys:
        superMod *= monkey.getTest()
    return superMod


def fullMonkeyPrint(monkeys):
    for monke in monkeys:
        monke.printMonkey()

start()