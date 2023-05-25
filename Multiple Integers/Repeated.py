# Give an unsorted integer array A and its Integer value X, find if X is found more then once in A:

def Is_repeated(Array,X):

    flag=False
    count=0
    for i in Array:

        if i==X:
            count+=1

            if count==2:
                flag=True
    return flag


 # Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The Given array is: " ,Array)

#X=input("Enter the search Elements: ")

#print ("The Index of the given Search elements is: " ,Is_repeated(Array,X))
