# Return the prime number from the given array:

import math

def Isprime(N):
    flag=True
    if (N<=1):
        flag=False
    if (N==2):
        return flag
        
    for i in range(2,int(math.sqrt(N)+1)):

        if (N%i==0):
            flag=False
            break
    return flag

def prime_array(Array):

    prime_array=[]

    for a in Array:
        if (Isprime(a)):
            prime_array.append(a)

    return prime_array

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The prime number of the given array is", prime_array(Array))

