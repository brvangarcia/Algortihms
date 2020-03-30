# Bubble Sort Algorithm
def bubbleSort(arr):
    #get array length
    arrayLength = len(arr)
    #loop thought all the array
    for j in range(arrayLength):
        #max item to check in array
        for i in range(0, arrayLength-j-1):
            #first item larger than second
            if arr[i] > arr[i+1]:
                #swap items
                arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [64, 34, 25, 193993, 22, 3939, 93] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),