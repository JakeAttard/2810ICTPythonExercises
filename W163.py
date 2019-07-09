from PyTest import *
##///////////////////////// PROBLEM STATEMENT //////////////////////////
## Given three ints, a b c, one of them is small, one is medium and   //
## one is large. Print True if the three values are evenly spaced,    //
## so the difference between small and medium is the same as the      //
## difference between medium and large.                               //
##   2 4 6 -> True                                                    //
##   4 6 2 -> True                                                    //
##   4 6 3 -> False                                                   //
##//////////////////////////////////////////////////////////////////////

a = int(input())
b = int(input())

if b > a:
    a,b = b,a

c = int(input())

if c > a:
    a,b,c = c,a,b
elif c > b:
    a,b,c = a,c,b

if a-b == b-c:
    print(True)
else:
    print(False)