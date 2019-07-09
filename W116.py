from PyTest import *
##/////////////////////////// PROBLEM STATEMENT /////////////////////////
## Write a program which accepts a time interval in hours, minutes and //
## seconds and prints the equivalent time in just seconds. One hour is //
## 3600 seconds and one minute is 60 seconds.                          //
##                                                                     //
##   hours  minutes  seconds     Total seconds                         //
##     1       10       20    ->    3680                              //       
##///////////////////////////////////////////////////////////////////////

list = []
i = 0

while i != 3:
    time = int(input())
    list.append(time)
    i += 1
totalSeconds = (list[0] * 3600) + (list[1] * 60) + list[2]
print(totalSeconds)
