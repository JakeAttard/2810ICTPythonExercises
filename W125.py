from PyTest import *
##//////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a Python program that, given a cost of an item (less than or equal //
## to one dollar), gives the number of 50 cent, 20 cent, 10 cent, 5 cent    //
## and 1 cent coins the buyer would receive if they handed over one dollar. //
## You must minimise the number of coins in the change.                     //
##////////////////////////////////////////////////////////////////////////////

c = int(input())
c = 100 - c

fifties = c//50
c = c - fifties * 50

twenty = c//20
c = c - twenty * 20

tens = c//10
c = c - tens * 10

fives = c//5
c = c - fives * 5

print(fifties, twenty, tens, fives, c)