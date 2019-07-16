# Compare the given array A and B and retruns the index upto which they are identical:

def identical(A,B):

    if (len(A)>len(B)):
        A,B=B,A

    for i in range(0,len(A)):

        index=i
        if not (A[i]==B[i]):
            index=i-1
            break
        index=(len(A)-1)
    
    return index


# Getting Input from User:

#N=input("Enter the number of elements in Array A: ")

#A=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array A: ")

    #A.append(Elements)

# Getting Input from User:

#N=input("Enter the number of elements for Array B: ")

#B=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array B: ")

    #B.append(Elements)

#print("The given Array A is", A)

#print("The given Array B is", B)

#print("The identical elements in the given array A and B upto the index of: ",identical(A,B))
