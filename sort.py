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

#选择排序入队
#时间复杂度O(N^2) 
#空间复杂度O(1)
def selectSort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[j] < arr[min]:
                min = j
        
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]
    return arr

#插入排序入队
#时间复杂度O(N^2)
# 空间复杂度O(1)
def insertSort(arr):
    n =  len(arr)
    if n < 1:
        return arr

    for i in range(1, n):
        key = arr[i]
        j = i
        while j > 0 and key < arr[j-1]:
           arr[j] = arr[j-1]
           j-=1
        arr[j] = key        
    return arr

#   快速排序
# 时间复杂度O(logN), 
# 空间复杂度O(NlogN)
def partation(arr, left, right):
    #将左边第一个数定为key
    key = left
    #只要left 和right 向中间移动没有相遇
    while left<right:
        while left < right and arr[right] >= key:
            right-=1
        while left < right and arr[left] <= key:
            left+=1
        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[key] = arr[key], arr[left]
    return left
    

def quickSort(arr, left, right):
    
    if left > right:
        return
    mid = partation(arr, left, right)
    quickSort(arr, left, mid-1)
    quickSort(arr, mid+1, right)

def quickSortMain(arr):
   return quickSort(arr, 0, len(arr)-1)

if __name__ == "__main__":
    pass