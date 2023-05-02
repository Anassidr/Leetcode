def quicksort(arr):
    return qs(arr, 0, len(arr)-1)

def qs(arr, l, r):
    if l >= r:
        return 
    p = partition(arr,l ,r)
    qs(arr, l, p-1)
    qs(arr, p+1, r)

# partition and return the index of the pivot
def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

a = [-3,-4,3,2,199,0]
quicksort(a)
print(a)

