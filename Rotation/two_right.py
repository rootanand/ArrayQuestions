# Rotate the given array to the right by two positions:

def Two_right(Array):

    #rotate=[]
    position=0

    #To rotate right by two bits:
    while not (position>=2):
         
        X=Array.pop(-1)
        Array.insert(0,X)
        position+=1

    #for a in Array:
        #rotate.append(a)

    #return rotate
    return Array

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The rotation of the given array by the two positions to the right is:",Two_right(Array) )

