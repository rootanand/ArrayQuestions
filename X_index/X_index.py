# Given an unsorted integer array A and an integer value X, 
# return the index at which X is located in A or return -1 if it is not found in A.

def X_index(Array,X):

    for i in Array:

        if(i==X):

            Index=Array.index(X)
            break
        Index=-1

    return Index

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The Given array is: " ,Array)

#X=input("Enter the search Elements: ")

#print ("The Index of the given Search elements is: " ,X_index(Array,X))

    
