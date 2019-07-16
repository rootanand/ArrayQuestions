#Given an unsorted integer array A and a value X, check if there exists a subset of A of size two that adds upto X and print the values that adds upto X.

def Subset_Values(Array,X):

    Length=len(Array)
    Subset=[]

    #Primary Index = I
    #Secondary Index = J

    I=0

    while not (I==Length):

        J=I+1

        while not (J==Length):


            if (Array[I]+Array[J]==X):
               Values ={Array[I],Array[J]}
               Subset.append(Values)

            J=J+1

        I=I+1

    return Subset

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#X=input("Enter the Sum: ")

#print("The Subset of Given Array is:",Subset_Values(Array,X))