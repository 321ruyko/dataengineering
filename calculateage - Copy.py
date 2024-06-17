import numpy as np
c=np.array([[1,2,3],
           [11,22,23]])
d=np.array([[1,2,3],
           [11,22,23]])
print('Minimum value',c.min(axis=1))
print("Maximum value",c.max(axis=1))
print("Sorted value",np.sort(c))
print("Mean ",c.mean(axis=1,dtype=int))
print("new row",np.concatenate((c,d),axis=1))
print("new coloumn",np.concatenate((c,d),axis=0))
print("Mult",np.multiply(c,d))
print("Reverse",np.flipud(c))


f=np.array(range(0,20)).reshape(4,5)

f[f%2==0]=0
f[f%2==1]=1

print(f)


