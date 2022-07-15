# Perkalian matrix

# penjelasan Perkalian matrix
# atau link: https://youtu.be/z6xfiHUuWWQ

import  numpy as np

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2]) # matrix satuan dengan 2 kolom dan 2 baris
print('matriks a:')
print(a)
print('matriks b:')
print(b)

# perkalian matrix
c1 = np.dot(a,b) # marix a dikali b
c2 = a.dot(b) # objek b dimasukkin fungsi dot yang nempel di objek a. dan hasilnya sama saja seperti c1

print('matriks c1:')
print(c1)
print('matriks c2:')
print(c2)
# perkalian matrix harus/apapun jumlah kolom dalam baris harus sama dengan baris kebawah
# atau matrix pertama barisnya harus sama dengan kolom matrix kedua
# pusing ahh