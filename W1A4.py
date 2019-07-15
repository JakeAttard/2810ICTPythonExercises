from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the  concatenation creates a double-char,   //
## then omit one of the chars, so "abc" and "cat" yields "abcat".            //
##   "abc", "cat" -> "abcat"                                                 //
##   "dog", "cat" -> "dogcat"                                                //
##   "abc", "" -> "abc"                                                      //
##/////////////////////////////////////////////////////////////////////////////

a = input()
b = input()

if not a:
    print('')
elif not b:
    print('')
else:
    print("".join([a, b]))