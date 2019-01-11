# Find the length of the given array:

def lengthofarray(A):

    
    count=0

    while(A[count:]):
        count+=1

    return count
A=[2,54,1,5,67,3]
print(lengthofarray(A))
