# Remove the Duplicates from the given array:

def duplicates(Array):

    duplicates_removed=[]

    for a in Array:
        if a not in duplicates_removed:
            duplicates_removed.append(a)

    return duplicates_removed

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The array without duplicates:", duplicates(Array))