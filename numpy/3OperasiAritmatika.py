# Operasi Aritmatika
# basicnya semua operasi aritmatika dinumpy itu adalah elementwise operation (operasinya per element)

import  numpy as np

# list biasa dari python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
# array di numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

## elementwise operation = operasinya per element
# penjumlahan
 #hasil = a+b # jika list biasa ditambahkan maka ditambah kan di ujungnya
hasil1 = anp+bnp # jika ditambahkan maka perkomponen ditambah

# pengurangan
 #hasil = a - b # jika list biasa tidak bisa dikurang
hasil2 = anp - bnp # dikurang perkomponen

# perkalian
 #hasil = a * b # jika list biasa tidak bisa dikurang
hasil3 = anp * bnp # dikali perkomponen

# pembagian
 #hasil = a / b # jika list biasa tidak bisa
hasil4 = anp / bnp

#kuadrat
hasil5 = anp**2

# multidimensi array numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9,],[-1,-2,-3]))

hasil6 = c + d #ditambahkan perkomponen
hasil7 = c * d #dikali perkomponen (ini bukan perkalian matrix)

print(hasil7)