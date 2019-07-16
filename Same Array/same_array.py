#Find the both array are same:

def Is_same(A,B):

    flag=True

    if (len(A)!=len(B)):
        flag=False

        for a in A:
            for b in B:
                if (a!=b):
                    flag=False
                    break
    
    return flag

# Getting Input from User:

#M=input("Enter the A elements: ")

#A=[]

#for a in range(0,M):

    #A_Elements=input("Enter the Elements in Array: ")

    #A.append(A_Elements)


#N=input("Enter the B elements: ")

#B=[]

#for b in range(0,N):

    #B_Elements=input("Enter the Elements in Array: ")

    #B.append(B_Elements)


#print("The given Array (A) is", A)

#print("The given Array (B) is", B)

#print("The given arrays A and B are same", Is_same(A,B))
