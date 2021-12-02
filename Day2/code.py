#!/usr/bin/env python3


with open("./input.txt", "r") as content:
    #For each line of the text file, strip the newline character, convert to integer, save to a list array
    lines = [line.rstrip('\n') for line in content.readlines()]

    forwardList = []
    upList = []
    downList = []

    for line in lines:
        if "forward" in line:
            for chars in line:
                if chars.isdigit():
                    forwardList.append(int(chars))

        if "up" in line:
            for chars in line:
                if chars.isdigit():
                    upList.append(int(chars))
      
        if "down" in line:
            for chars in line:
                if chars.isdigit():
                    downList.append(int(chars))

    forwardSum = sum(forwardList)
    upSum = sum(upList)
    downSum = sum(downList)

    height = (downSum - upSum) 

    ans = (height * forwardSum)
    print("Part One Answer: ", ans)




    #---------------Part TWO-------------------

    
    horz = 0
    depth = 0
    aim = 0

    #Iterate Through List
    for line in lines:
        #If line contains forward, extract integer, add it to Horizontal, multiply current element integer by current aim and add it to Depth
        if "forward" in line:
            for chars in line:
                if chars.isdigit():
                    horz += int(chars)
                    depth += (aim * int(chars))

        #If Line contains up, extract integer, decrease aim
        if "up" in line:
            for chars in line:
                if chars.isdigit():
                    aim -= int(chars)

        #If Line contains up, extract integer, increase aim
        if "down" in line:
            for chars in line:
                if chars.isdigit():
                    aim += int(chars)


#Multiply Depth by Horizontal
print("Part two answer: ", (depth*horz))
