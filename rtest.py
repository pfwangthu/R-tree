#!/usr/bin/python
# -*- coding: utf-8 -*-
from rtree import *
from random import uniform
from time import time
data = {}
#初始化10000个坐标在(-1000, 1000)间，面积为0.01的矩形。
for i in range(100000):
    x = uniform(-1000, 1000)
    y = uniform(-1000, 1000)
    data[i] = {'xmin':x, 'xmax':x + 0.01, 'ymin':y, 'ymax':y + 0.01}
#设置一个根节点，m=3，M=7
root = Rtree(m = 3, M = 7)
n = []

for i in range(100000):
    n.append(node(MBR = data[i], index = i))
t0 = time()
#插入
for i in range(100000):
    root = Insert(root, n[i])
t1 = time()
print 'Inserting ...'
print t1 - t0
#搜索
x = root.Search(merge(n[0].MBR, n[1].MBR))
t2 = time()
print 'Searching ...'
print t2 - t1
#删除
for i in range(100000):
    root = Delete(root, n[i])
t3 = time()
print 'Deleting ...'
print t3 - t2
