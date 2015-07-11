import sys

def binary_search(arr, target):
    min = 0
    max = len(arr)
    mid = (min + max) / 2

    
    if target == arr[mid]:
        print "Target {} was found in the array".format(target)
    elif target < arr[mid]:
        arr = arr[:mid]
        if len(arr) == 1:
            print "Target {} not found in the array".format(target)
            sys.exit()
        binary_search(arr, target)
    elif target > arr[mid]:
        arr = arr[mid:]
        if len(arr) == 1:
            print "Target {} not found in array".format(target)
            sys.exit()
        binary_search(arr, target)
 




    
