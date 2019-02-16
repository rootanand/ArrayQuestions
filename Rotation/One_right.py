# Rotate the given array by moving one position:

def One_left(Array):

    rotate=[]
    X=Array.pop(-1)

# To rotate one bit by left:
    rotate.append(X)
    for a in Array:
        rotate.append(a)

    return rotate

 #Getting Input from User:

N=input("Enter the number of elements: ")

Array=[]

for a in range(0,N):

    Elements=input("Enter the Elements in Array: ")

    Array.append(Elements)

print("The given Array is", Array)

print("The first rotation of the given array is",One_left(Array))