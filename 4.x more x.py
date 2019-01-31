def more_then_once(array,x):
    flag=False
    count=0
    for i in array:
        if i==x:
            count+=1
            if count>1:
                flag=True
    return flag
array=[1,2,3,5,5,6,7,8]
x=input("enter the value:")
print(more_then_once(array,x))
