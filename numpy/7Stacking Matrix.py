# Stacking Matrix
# hati hati ukuran dari matrix akan mempengaruhi oprasinya

import  numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
# yang matrix
aMat = np.zeros((2,3))
bMat = np.ones((2,3))


# Stacking Matrix = menumpuk matrix

c = np.hstack((a,b)) #hstack = horizontal stack = berbaris. (a,b) = a nya yang awal dan b yang diakhir/diujung/dibelakang
d = np.vstack((a,b)) #vertical stack = kebawah. (a,b) = a nya yang awal dan b yang diakhir/diujung/dibelakang
# yang matrix
cMat = np.hstack((aMat,bMat)) #hstack = horizontal stack = berbaris.
dMat = np.vstack((aMat,bMat)) #vertical stack = kebawah.
print(cMat)