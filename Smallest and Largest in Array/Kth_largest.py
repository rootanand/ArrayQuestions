# Find the Kth largest and smallest number in the given array:

import Largest

def Kth_Largest(Array,K):

	Descending=[]
	Length=len(Array)
	count=0

	while not(count==Length):

		X=Largest.Largest_in_Array(Array)
		Descending.append(X)
		Array.remove(X)
		count+=1

	Result=Descending[K-1]
	return Result

# Getting Input from User:

#N=input("Enter the number of elements: ")

#Array=[]

#for a in range(0,N):

    #Elements=input("Enter the Elements in Array: ")

    #Array.append(Elements)

#print("The given Array is", Array)

#K=input("Enter the value of K: ")

#print("The given Kth Largest number in the given array is",Kth_Largest(Array,K) )








