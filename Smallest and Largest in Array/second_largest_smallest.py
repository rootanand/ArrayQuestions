# Find the second largest number in the given array:

def second_largest(Array):

    Largest=Array[0]
    Second_largest=Array[1]

    for a in Array:

        if (a>Largest):
            
            Second_largest=Largest
            Largest=a

        elif (a==Largest):
            Largest=a

        elif (a>Second_largest):
            Second_largest=a

    return Second_largest

def second_smallest(Array):

    Smallest=Array[0]
    Second_smallest=Array[1]

    for a in Array:

        if (a<Smallest):
            
            Second_smallest=Smallest
            Smallest=a

        elif (a==Smallest):
            Smallest=a

        elif (a>Second_smallest):
            Second_smallest=a

    return Second_smallest

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The second largest number of the given array is", second_largest(Array))
#print("The second smallest number of the given array is", second_smallest(Array))