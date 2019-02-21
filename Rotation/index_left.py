# Find the 3rd index of the given array after two rotations:

def Left_Index(Array):

    rotation=1
    
    while not (rotation>2):

        X=Array.pop(0)
        Array.append(X)
        rotation+=1
    
    Value=Array[3]
    return Value

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The third index of the given array after two rotations:",Left_Index(Array) )