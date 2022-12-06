def main():
    testIn = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    input = open("./input.txt", "r").read()
    print(findEncoded(input))

def findEncoded(string):
    marker = ""
    chars = 0
    markerLength = 14
    for char in string:
        if len(marker) >= markerLength:
            if allDifferent(marker):
                return chars
            else:
                marker = switchChars(marker, char)
        else:
            marker+=char
        chars+=1

def allDifferent(code):
    for i in range(len(code)):
        for j in range(len(code)):
            if not i==j:
                if code[i] == code[j]:
                    return False
    return True

def switchChars(string, char):
    newStr = string[1:]
    newStr += char
    return newStr

main()