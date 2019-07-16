def by_left(Array,K):

    position=1

    while not (position>K):

        X=Array.pop(0)
        Array.append(X)
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

#print("The left rotations of the given array is", by_left(Array,K))