# Find the even number in the given array:

def Even_numbers(Array):

    Even_array=[]
    for a in Array:

        if (a%2==0):
            Even_array.append(a)

    return Even_array

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Even number of the given array is", Even_numbers(Array))