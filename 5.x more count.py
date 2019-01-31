def more_then_once_count(array,x):
    
    count=0
    for i in array:
        if i==x:
            count+=1
    
               
    return count 
array=[1,2,3,5,5,5,5,5,6,7,8]
x=input("enter the value:")
print(more_then_once_count(array,x))
