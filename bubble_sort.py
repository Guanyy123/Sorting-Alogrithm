##冒泡排序
def bubbleSort(arr):
    n = len(arr)
    if n < 1:
        return arr
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:   
              arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr