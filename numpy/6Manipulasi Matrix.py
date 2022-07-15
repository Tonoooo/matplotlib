# Manipulasi Matrix

import  numpy as np

a = np.array(([1,2,3],
              [4,5,6]))

# shape = ukuran
print('matriks a dengan ukuran: ',a.shape) # shape itu ngambil ukuran
print(a)

# transpose matrix = baris dijadiin kolom
print('transpose matrix a:')
print(a.transpose())# cara pertama
print(np.transpose(a))# cara kedua
print(a.T)# cara ketiga

# flatten array/vektor baris = disejejerin/dibarisin
print('flatten matrix a:')
print(a.ravel())
print(np.ravel(a))# cara kedua

# reshape matrix  syaratnya jumlah komponennya harus sama
print('reshape matrix a:')
print(a.reshape(3,2)) # 3 baris 2 kolom. dan ini berbeda dgn transpose kalo transpose kolomnya berurutan, kalo ini barisnya berurutan
print(a.reshape(6,1)) # 6 baris 1 kolom

# resize matrix
print('resize matrix a:')
#print(a.resize(3,2)) # ini tidak bisa karna resize tidak mengembalikan nilai tapi dia akan merubahnya
a.resize(3,2) # 3 baris 2 kolom. harus seperti ini karna resize
print(a) #resize sama kaya reshape tapi dia akan merubah a dan ini berbeda dgn transpose kalo transpose kolomnya berurutan, kalo ini barisnya berurutan
print('matriks a dengan ukuran: ',a.shape)