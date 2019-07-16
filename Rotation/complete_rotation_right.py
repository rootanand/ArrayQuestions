# Write the rotation code for the given for one complete Rotations:
# Without using Inbuilt functions.

def complete_rotation_right(Array):

    count=0
    while not (count==len(Array)):

        index=-1
        swap=0
        while not (index==len(Array)):
            Array[index],swap=swap,Array[index]
            index+=1
        count+=1
    return Array

Array=[1,2,3,4,5]
print complete_rotation_right(Array)