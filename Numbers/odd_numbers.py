# Return the odd numbers in the given array:

def Odd_numbers(Array):

    Odd_array=[]
    for a in Array:

        if not (a%2==0):
            Odd_array.append(a)

    return Odd_array

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Odd numbers in the given array is", Odd_numbers(Array))