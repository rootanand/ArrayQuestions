# Find the count of the values which is greater than or equal to the given integer:

def Is_Greater(Array,Integer):

    count=0

    for a in Array:

        if (a>=Integer):
             count+=1
    
    return count

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#Integer=input("Enter the integer value: ")

#print("The count is: ",Is_Greater(Array,Integer))

        