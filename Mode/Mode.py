# Find the mode of the given array:

def Mode(Array):

    count=0
    maxcount=0
    mode=0

    for a in Array:
        
        for b in Array:
            if(a==b):
                count+=1

        if (count>maxcount):
            maxcount=count
            mode=a

    return mode


#Getting Input from User:

N=int(input("Enter the number of elements: "))

Array=[]

for a in range(0,N):

    Elements=int(input("Enter the Elements in Array: "))

    Array.append(Elements)

print("The given Array is", Array)

print("The Mode of given array is", Mode(Array))