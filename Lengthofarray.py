# Find the length of the given array:

def lengthofarray(A):

    count=0

    while(A[count:]):
        count+=1

    return count

N=input("Enter the Number of elements: ")

A=[]

for a in range (0,N):
    
	X = input("Enter the Numbers: ")
    
	A.append(X)

print A


print("The length of the given array is: ")
print(lengthofarray(A))
