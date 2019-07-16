# Rotate the given array by one position to the left:

def One_left(Array):

    #rotate=[]
    X=Array.pop(0)

    #for a in Array:
        #rotate.append(a)

    #To Rotate Left:
    Array.append(X)

    return Array

 #Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The one bit left rotation of the given array is:", One_left(Array))