from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Say that a "clump" in a list is a series of 2 or more adjacent elements   //
## of the same value. Print the number of clumps in the given list.          //
##    1, 2, 2, 3, 4, 4  -> 2                                                 //
##    1, 1, 2, 1, 1  -> 2                                                    //
##    1, 1, 1, 1, 1  -> 1                                                    //
##/////////////////////////////////////////////////////////////////////////////

numArray = []

for i in range(int(input())):
    numArray.append(int(input()))

last = None
sameNum = False
clumps = 0

for i in numArray:
    if last == i:
        if not sameNum:
            clumps += 1
            sameNum = True
    else:
        sameNum = False

    last = i

print(clumps)