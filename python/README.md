### 排序


- Quicksort:
```
'''
1. 从数列中挑出一个元素，称为 “基准”（pivot），
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。 在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

low middle hight key
if key > middle ==> low = key; key = middle .... 
'''
def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            array[low] = array[high]
            low += 1
            array[high] = array[low]
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)
```

- Bubble Sort:
```
def Dubble_sort(a):
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
return a
```

- Selection sort
```
def Selection_sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        if min != i:
            a[min], a[i] = a[i], a[min]
    return a
```


- Insertion sort
```
def Insertion_sort(a):
    for i in range(1,len(a)):
        j = i
        while j>0 and a[j-1]>a[i]:
            j -= 1
        a.insert(j,a[i])
        a.pop(i+1)
    return a
```
