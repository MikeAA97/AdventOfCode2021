#!/usr/bin/env python3

def checkElements(list):
    ans = 0
    #Iterate through list, with x being index, y being the value
    for x, y in enumerate(list[:-1]):
    #if the next element (index + 1) is greater than the current value increment answer
        if list[x+1] > y:
            ans += 1
    return ans



with open("./input.txt", "r") as content:
    #For each line of the text file, strip the newline character, convert to integer, save to a list
    lines = [int(line.rstrip('\n')) for line in content.readlines()]
    print(checkElements(lines))

    #Take the list of integers, sum every 3 elements, and save to new list
    addedLines = ([sum(lines[i:i+3]) for i in range(0, len(lines))])
    print(checkElements(addedLines))
