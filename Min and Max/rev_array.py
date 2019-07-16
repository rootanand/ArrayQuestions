# The reverse of the given array:

def Rev_array(Array):

    Reverse=[]
    index=1
    Length = len(Array)

    while (index!=Length):

        elements=(Array[-index]) 
        Reverse.append(elements)
        index+=1

    Reverse.append(Array[0])
    return Reverse

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The reverse order of the given array is:", Rev_array(Array))