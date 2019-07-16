# Rotate the given array by R positions and find the Integer in the given index I:

def by_right(Array,R,I):

    Rotation=1

    while not (Rotation>R):

        X=Array.pop(-1)
        Array.insert(0,X)
        Rotation+=1

    Value=-1

    if (I<len(Array)):
        Value=Array[I]
    return Value




# Getting Input from User:

#R=input("Enter the number of Rotations: ")

#I=input("Enter the index: ")

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The I index of the given array after R rotations is", by_right(Array,R,I))
