# Rotate the given array by K positions:

def by_right(Array,K):

    position=1

    while not (position>K):

        X=Array.pop(-1)
        Array.insert(0,X)
        position+=1

    return Array

# Getting Input from User:

#K=input("Enter the number of Rotations: ")

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The right rotations of the given array is", by_right(Array,K))
