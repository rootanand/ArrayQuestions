N=3
mod_count=0
count = 0
I=0

Index = [1,2,3,4,5,6,7,8,9,10]

while not (count==len(Index)):
    
    Dictionary = {0:0}
    
    if I>N:
        
        I=0
    
        if mod_count%N==0:

            Dictionary[count+1]=Index[I]

            count+=1
            mod_count+=1
            I+=1
        
    mod_count+=1
    I+=1
        
print Dictionary
        