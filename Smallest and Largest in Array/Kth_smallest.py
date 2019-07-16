# Find the Kth largest and smallest number in the given array:

import Smallest

def Kth_Smallest(Array,K):

	Ascending=[]
	Length=len(Array)
	count=0

	while not(count==Length):

		X=Smallest.Smallest_in_Array(Array)
		Ascending.append(X)
		Array.remove(X)
		count+=1

	Result=Ascending[K-1]
	return Result

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#K=input("Enter the value of K: ")

#print("The given Kth Smallest number in the given array is",Kth_Smallest(Array,K) )

