#coding:utf8
'''
reproduce http://www.cnblogs.com/Liqiongyu/p/5911613.html
随机生成0~10000000之间的数值
'''
import copy
import random

import time

import numpy as np


def Insertion_sort(a):
    for i in range(1,len(a)):
        j = i
        while j>0 and a[j-1]>a[i]:
            j -= 1
        a.insert(j,a[i])
        a.pop(i+1)
    return a

def Selection_sort(a):
    for i in range(len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[min] > a[j]:
                min = j
        if min != i:
            a[min], a[i] = a[i], a[min]
    return a

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

def Dubble_sort(a):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
    return a


def Quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        Quick_sort(array,low,key_index)
        Quick_sort(array,key_index+1,high)

def getrandata(num):
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,10000000))
        i+=1
    return a

'''
随机生成20个长度为10000的数组
'''
a = []
for i in range(20):
    a.append(getrandata(10000))

'''
测试时间函数
'''
def time_it(f,a):
    t = []
    for i in range(len(a)):
        t1 = time.time()
        f(a[i])
        t2 = time.time()
        t.append(t2-t1)
    return t
tt1 = time_it(Selection_sort,copy.deepcopy(a))
tt2 = time_it(Dubble_sort,copy.deepcopy(a))
tt3 = time_it(Insertion_sort,copy.deepcopy(a))
tt4 = time_it(Quick_sort,copy.deepcopy(a))
print np.mean(tt1),tt1
print np.mean(tt2),tt2
print np.mean(tt3),tt3
print np.mean(tt4),tt4