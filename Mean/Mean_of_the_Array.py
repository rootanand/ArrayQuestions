# Find the mean of the given unsorted Array:

def Mean_of_Array(Array):

    A=len(Array)
    sum=0

    for a in Array:
        sum+=a

    Mean=sum//A
    return Mean

    # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Mean value of given array is", Mean_of_Array(Array))