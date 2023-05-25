# 50. Given an unsorted integer array A, find the sum and product of the minimum and maximum values of the array. 

import Largest

import Smallest



def minmax(Array):

    Max=Largest.Largest_in_Array(Array)
    Min=Smallest.Smallest_in_Array(Array)

    Sum=Min+Max
    Product=Min*Max

    print("The Sum of Minimum and Maximum Value is: ", Sum)
    print("The Prouduct of Minimum and Maximum Value is: ",Product)

# Getting Input from User:

N=input("Enter the number of elements: ")

Array=[]

for a in range(0,N):

    Elements=input("Enter the Elements in Array: ")

    Array.append(Elements)

print("The given Array is", Array)

minmax(Array)


