# Print the elements in the given array by the reverse order:

def Rev_elements(Array):

    
    index=1
    Length = len(Array)


    while (index!=Length):

        elements=(Array[-index]) 
        print elements
        index+=1

    print Array[0]

# Getting Input from User:

N=input("Enter the number of elements: ")

Array=[]

for a in range(0,N):

    Elements=input("Enter the Elements in Array: ")

    Array.append(Elements)

print("The given Array is", Array)

Rev_elements(Array)