import random
import math 

def MergeSort(arr):
    flips = 0
    if len(arr) > 1:
        #find midpoint of array
        mid = len(arr)//2
        
        #split the array into 2 halves (left & Right)
        L = arr[:mid]
        R = arr[mid:]
        
        #Recursively call merge sort and left & right
        MergeSort(L)
        MergeSort(R)
        
        i = j = k = 0
        
        #copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
                flips+=1
            k+=1
            
        #check if any elemnt is leftover
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
            
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1
    print(flips)

def bubbleSort(arr):
    k = len(arr)
    flips = 0
    
    #Traverse through all array elements
    for i in range(k):
        #Last i elements are already in place 
        
        #Traverse array from 0 to n-i-1
        for j in range(0, k-i-1):
            
            #if the element found is greater than next element
            if arr[j] > arr[j+1]:
                
                #then swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flips += 1
    print(flips)

n = 2**17
A = list(range(1, n))
print(n)

random.shuffle(A)

MergeSort(A)
bubbleSort(A)