
def countarray(a):
    count=0
    
    while(a>0):
        temp=a%10
        count+=1
        a=a//10
    return count
a=(1234)
print(countarray(a))
