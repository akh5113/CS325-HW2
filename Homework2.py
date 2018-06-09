# Anne Harris harranne@oregonstate.edu
# CS 325 -400
# Homework 2 - Stooge Sort

import math

# open up data.txt file
# IMPORT FILE
# File I/O based of off implementation discussed on Slack
nums = []
with open("data.txt", "r") as f:
    for x in f:
        var = x.split(" ")
        for y in range(len(var)):
            var[y] = int(var[y])    # string into integer
        nums.append(var[1:])        # we don't want first number as it's the count of the line

f.close()

print("Merge Sort")
# print from file
arraySize = len(nums)
# print the unsorted arrays
print("The unsorted arrays are: ")
for a in range(arraySize):
    print(nums[a])


# implement Stoogesort
# Based off of pseudo code in Week 2 Homework and on the Stooge Sort wikipedia linked below
# https://en.wikipedia.org/wiki/Stooge_sort
def StoogeSort(array, start, end):
    # check to see if array has two elements
    # and check if the first element is bigger than the second
    numElms = (end - start + 1)
    # if there are only two elements in the array, compare them
    if numElms == 2:
        # if the first element is bigger than the second, swap them
        if array[start] > array[end]:
            # swap elements
            array[start], array[end] = array[end], array[start]
    if numElms > 2:
        m = int(numElms/3)
        # first two thirds
        StoogeSort(array, start, (end - m))
        # second two thirds
        StoogeSort(array, (start + m), end)
        # first two thirds again
        StoogeSort(array, start, (end - m))

# Sort the arrays using Stooge Sort
for listS in nums:
    StoogeSort(listS, 0, (len(listS)-1))

print("The sorted arrays are: ")
for i in range(arraySize):
    print(nums[i])

# store sorted lists in .txt output
fOut = open("stooge.out", "w+")
for nLine in range(arraySize):
    number = nums[nLine]
    for x in range(len(number)):
        fOut.write(str(number[x]))
        fOut.write(" ")
    fOut.write("\n")
fOut.close()