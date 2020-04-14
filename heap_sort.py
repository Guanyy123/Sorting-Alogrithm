import random
#判断局部的形成正确的heap
def heapfy(tree, n, root):
    c1 = 2*root+1
    c2 = 2*root+2
    max_num = root
    if c1 < n and tree[c1] > tree[max_num]:
        max_num = c1
    if c2 < n and tree[c2] > tree[max_num]:
        max_num = c2
    if max_num != root:
        #swap比头节点小的heap，作交换
        tree[max_num], tree[root]= tree[root], tree[max_num]
        heapfy(tree, n, max_num)

#将顺序混乱的arry组成符合要求的heap
def build_heap(tree, n):
    last_parent = (n-2)//2
    for i in range(last_parent, -1, -1):
        heapfy(tree, n, i)
        

def sort(tree, n):
    build_heap(tree, n)
    i= n-1
    for i in range(i,-1,-1):
       tree[0], tree[i]=tree[i], tree[0]
       heapfy(tree, i, 0)
    return tree

#堆排序在建堆的时候时间复杂度是线性的，为O(N)。
#对调整的递归实现时间复杂度为           O(logN)
#整体算法的时间复杂度为                 O(NlogN)
if __name__ == "__main__":
   tree = [2,5,3,1,10,4]
   b = [random.randint(1,1000) for i in range(1000)]
   print(sort(b, 1000))