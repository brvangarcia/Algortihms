#Quick Sort
def partition(arr, low, high):
    #i = smallest item
    i = low - 1
    #pivot will be highest number
    pivot = arr[high]
    #loop thought the smallest to highest
    for j in range(low,high):
        #current element smaller than pivot
        if arr[j] < pivot:
            #add one to i
            i = i +1
            #swap arr i with arr j, arr j with arr i
            arr[i], arr[j] = arr[j], arr[i]
    #arr i + 1 = highest number, highest number = arr i + 1
    arr[i+1], arr[high] = arr[high], arr[i+1]
    #return i + 1
    return i + 1

def quickSort(arr,low,high):
    #if high number is higher than lower
    if low < high:
        #arrange items so pivot is the middle item
        pi = partition(arr, low, high)
        #sort elements before partition
        quickSort(arr, low, pi -1)
        #sort elements after partition
        quickSort(arr, pi+1, high)

arr = [1012342342134123412343, 7, 8, 9, 112341234, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 