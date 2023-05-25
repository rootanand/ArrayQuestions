# Return the copy of the given unsorted array:

def copy(Array):

    C=[]
    for a in Array:
        C.append(a)

    return C

#Getting Input from the user:

N=int(input("Enter the number of elements: "))

Array=[]

for a in range(0,N):

    Elements=int(input("Enter the Elements in Array: "))

    Array.append(Elements)

print("The given Array is", Array)

print("The copy of the given array is", copy(Array))
