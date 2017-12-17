import numpy as np
a = np.array([10,20,30,40]).reshape([2,2])
b = np.arange(4).reshape([2,2])
c = a==30
r = np.random.random([2,2])
print(np.sum(a,axis=0))
print(np.min(a))
print(np.min(a))
print(np.argmax(a))
print(np.mean(a),a.mean())#平均数
print(np.median(a))#中位数
print(np.cumsum(a))#累积
print(np.diff(a))#累差
print(np.nonzero(a))#非零数的位置
print(np.sort(a))#排序
print(np.transpose(a),a.T)#转置矩阵
print(np.clip(a,20,30))#截断
print(a[1])#第二行
print(a[1,:])#第二行所有数
print(a[:,1])#第二列所有数
print(a[1,0:1])#第二行数

for col in a.T:#遍历列
    print(col)

for item in a.flat:#遍历项
    print(item)

#矩阵合并
print(np.vstack((a,b)))
print(np.hstack((a,b)))
#加维度
one = np.array([1,1,1,1])
print(one[np.newaxis,:])
print(one[:,np.newaxis])
#多合并，可指定合并方向
ss = np.concatenate((a,b,b,a),axis=1)

print(ss)
#等量分割
a12 = np.arange(12).reshape([3,4])
print(a12)
print(np.split(a12,2,axis=1))
#不等量分割
print(np.array_split(a12,3,axis=1))
print(np.vsplit(a12,3))
print(np.hsplit(a12,2))