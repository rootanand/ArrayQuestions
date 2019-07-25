#Given an unsorted integer array A and an integer value X,
#  return the indices of the locations where X is found in A.

def Indices_of_X(Array,X):

    for i in range(0,len(Array)):

        if Array[i]==X:
            print (i)


 # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The Given array is: " ,Array)

#X=input("Enter the search Elements: ")

#Indices_of_X(Array,X)