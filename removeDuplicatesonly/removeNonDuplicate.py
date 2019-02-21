"""problem Statement :
   ===================
        To remove the Non Duplicte element from the array
        
Input :
=======
  Integer Array
Output :
========
  Contains non Duplicate elements
  
Code :
======
def removeDuplicate(array): # To remove the Duplicate Element form the Array
    j = 0
    i = 0
    count = 0
    lenght = getLenght(array) -1
    while(i!=lenght):
        if (array[i] != array[i+1]):
            array[j] = array[i]
            #print(array[i])
            count += 1
            j += 1
        i += 1
    
    array[j] = array[-1]
    array.append(count)
    return array
