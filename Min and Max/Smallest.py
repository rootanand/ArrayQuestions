# Find the smallest number in the given Array:

def Smallest_in_Array(Array):

    Smallest=2147483647
    
    for a in Array:
        if (a<Smallest):
            Smallest=a

    return Smallest

  # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Smallest number of the given array is", Smallest_in_Array(Array))

