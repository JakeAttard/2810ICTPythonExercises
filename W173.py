from PyTest import *
##//////////// PROBLEM STATEMENT ///////////////
## Write a program which takes a number n and //
## adds up the numbers in the range 0..n      //
##    3 -> 6                                  //
##   10 -> 55                                 //
##   20 -> 210                                //
##//////////////////////////////////////////////

n = int(input())
sum = 0
for i in range (0, n + 1):
    sum += i
print(sum)