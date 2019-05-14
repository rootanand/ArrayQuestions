# Find the Largest Number in the given Array:

def Largest_in_Array(Array):

    Largest=0
    
    for a in Array:
        if (a>Largest):
            Largest=a

    return Largest

  # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Largest number of the given array is", Largest_in_Array(Array))

