#Given an unsorted integer array A and a value X, check if there exists a subset of A of size two that adds upto X (Subset sum for a pair).

def Is_Exists(Array,X):

    Length=len(Array)
    flag=False

    #Primary Index = I
    #Secondary Index = J

    I=0

    while not (I==Length):

        J=I+1

        while not (J==Length):


            if (Array[I]+Array[J]==X):
                flag=True
                return flag

            J=J+1

        I=I+1

    return flag

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#X=input("Enter the Sum: ")

#print("The subset of size two that adds upto X is Exists:",Is_Exists(Array,X))






