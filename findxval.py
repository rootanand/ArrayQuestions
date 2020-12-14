def findx(array):
    flag=False
    for i in array:
        if(i==x):
            flag=True
    return flag
array=[1,3,5,7,9]
x=input("enter the value:")
print(findx(array))

