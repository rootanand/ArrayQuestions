import find_min
import FindLenght
import Max
def kth_smallest_ele(array,kthele):
    smallest_ele = 1
    iterator = 1
    lenght = FindLenght.count(array)
    while(iterator!=kthele):
        if lenght == kthele :
            return Max.Max(array)
        else:
            smallest_ele = find_min.findMin(array)
            for j in array:
                if (j == smallest_ele):
                    array.remove(smallest_ele)
            iterator += 1
        smallest_ele = find_min.findMin(array)
    return smallest_ele

array = [5,1,9,7,2,8,3,6,4]
kthele = 9
#print()
v = kth_smallest_ele(array,kthele)
print("The {0} Smallest Element in the array is {1}".format(kthele,v))