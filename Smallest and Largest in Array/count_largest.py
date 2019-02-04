# Count of the Largest number in the given array:

import Largest

def count_largest(Array):

    count=0
    X=Largest.Largest_in_Array(Array)   #X is the return value of Largest.py

    for a in Array:
        if (a==X):
            count+=1

    return count

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("Count of the largest number in the given array is", count_largest(Array))

