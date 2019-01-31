# Given an unsorted integer array A and an integer value X, return the number of times X is found in A.

def Count_Repeated(Array,X):

    count=0
    for i in Array:

        if i==X:
            count+=1

    return count


 # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The Given array is: " ,Array)

#X=input("Enter the search Elements: ")

#print ("The Index of the given Search elements is: " ,Count_Repeated(Array,X))