#Merge Sort
def mergeSort(arr):
    #check if array is empty
    if len(arr) > 1:
        #divide arrray in 2
        mid = len(arr)//2
        #left array
        left = arr[:mid]
        #right array
        right = arr[mid:]
        #divide left array
        mergeSort(left)
        #divide right array
        mergeSort(right)
        #variable declaration
        i = j = k = 0
        #check for arrays length larger than i and j
        while i < len(left) and j < len(right):
            # right array larger than left
            if left[i] < right[j]:
                #left array in position i = arr in postion k
                arr[k] = left[i]
                #i ++ to increase left array
                i+=1
            #left array larger than right
            else:
                 #right array in position i = arr in postion k
                arr[k] = right[j]
                #j ++ to increase right array
                j+=1
            #next item on array
            k+=1
        #while array left is greater than i
        while i < len(left):
            #left array = arr k
            arr[k] = left[i]
            #i ++ to increase left array
            i +=1
            #next item on array 
            k +=1
         #while array right is greater than i
        while j < len(right):
             #right array = arr k
            arr[k] = right[j]
            #j ++ to increase right array
            j +=1
            #next item on array 
            k +=1

def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i]) 
    print() 


arr = [12, 11, 13, 5, 6, 7]  
print ("Given array is", "\n")  
printList(arr) 
mergeSort(arr) 
print("Sorted array is: ", "\n") 
printList(arr) 