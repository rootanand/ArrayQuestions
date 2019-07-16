#49. Given an unsorted integer array A, check if the array A is a palindrome or not.

import rev_array

def Pallindrome(Array):

    flag=True

    Reverse=rev_array.Rev_array(Array)

    if not (Array==Reverse):

        flag=False
    
    return flag

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Given Array is pallindrome",Pallindrome(Array))

