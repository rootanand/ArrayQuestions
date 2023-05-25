# Find the perfect squares in the given array:

import math

def Is_perfect_sq(X):

    flag=True
    M=math.sqrt(X)
    N=round(M)

    if not (M==N):
        flag=False
    
    return flag

def perfect_sq_array(Array):

    sq_array=[]

    for a in Array:

        if (Is_perfect_sq(a)):
            sq_array.append(a)

    return sq_array

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The perfect squares in the given array is", perfect_sq_array(Array))
        
