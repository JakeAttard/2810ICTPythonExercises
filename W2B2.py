from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////
## Write a program that reads the file phillip.txt, counts the number of //
## words in the file, and prints out the count.                          //
##/////////////////////////////////////////////////////////////////////////

fileName = open("phillip.txt")
count = 0
for lines in fileName:
    for words in lines.split():
        count += 1
print(count)
fileName.close()