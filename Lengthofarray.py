# Find the length of the given array:

def lengthofarray(A):

    count=0

    while(A[count:]):
        count+=1

    return count
#N=input(str("Enter the Number of elements: "))

A=[]
X=int(input("Enter the Numbers: "))

while(X!="stop"):  
    A.append(X)

print A

print("The length of the given array is: ")
print(lengthofarray(A))
