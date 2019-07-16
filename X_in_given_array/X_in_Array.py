#  Given an unsorted integer array A and an integer value X, find if A contains the value X.

def X_in_array(Array,X):

    flag=False

    for i in Array:

        if (i==X):
            flag=True
            break

    return flag
            
# Getting input from User:

#X=input("Enter the search element: ")
#N=input("Enter the Number of elements: ")

#Array=[]

#for a in range (0,N):
    #Elements=input("Enter the input elements: ")
    #Array.append(Elements)

#print Array
#print(X_in_array(Array,X))

