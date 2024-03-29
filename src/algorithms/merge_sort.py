def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        # dividing into left array and right array from mid
        L = arr[:mid]
        R = arr[mid:]
        #recursion reducing the length of arrrays by dividing further
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            #comparing left and right array elements
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # if elements left out in left array or right array add it to the final array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

    
def sort(arr):
    sorted_arr = merge_sort(arr)
    return sorted_arr


