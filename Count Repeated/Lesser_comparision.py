# Find the count of the Integer in the given array and compare the array is less than or equal to the given Integer.

def Is_Lesser(Array,Integer):

    count=0

    for a in Array:

        if (a<=Integer):
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

#print("The count is: ",Is_Lesser(Array,Integer))
