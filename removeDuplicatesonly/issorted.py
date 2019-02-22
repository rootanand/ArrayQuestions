problem statement :
===================
    Function to check whether the given array is sorted or not 
Input :
=======
     Integer Array 
     
 Output :
 ========
    True - if sorted - Bool
    False - if not sorted - Bool
    
Code :
=====
import findLenght
def isSorted(array): # To Check whether array is sorted or not 
    
    flag = True
    lenght = findLenght.getLenght(array)

    if lenght == 0 or lenght == 1:
        return True
    iteratorValue = 0
    while (i!=lenght-1):
        if array[iteratorValue] > array[iteratorValue+1]:
            flag = False
        iteratorValue+=1
    return flag
