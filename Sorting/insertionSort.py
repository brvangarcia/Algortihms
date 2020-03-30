# Insertion Sort
def insertionSort(arr):
    #loop thought array
    for i in range(1, len(arr)):
        #starting point to swap
        key = arr[i]
        #starting value
        j = i - 1
        #while j is not the first or after key
        while j >= 0 and key < arr[j]:
            #swap item before the first one
            arr[j+1] = arr[j]
            #item before the swaped
            j -= 1
        #next point to swap
        arr[j+1] = key

arr = [1233, 11, 13, 3, 6] 
insertionSort(arr) 
for i in range(len(arr)): 
    print ("% d" % arr[i]) 