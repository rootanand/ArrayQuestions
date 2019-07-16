#Given an unsorted integer array A, print the contents of the array in the
#  given format: {arrayindex:value, arrayindex:value}.
#  Note that there is no comma after the last value. 

def Dictionary(Array):

    Dictionary={}
    X=len(Array)
    index=0

    while (index!=X):
        Dictionary[index]=Array[index]
        index+=1

    return Dictionary

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#print("The Array in the format", Dictionary(Array))
