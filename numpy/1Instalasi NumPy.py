# Numpy merupakan salah satu library pada Python yang berfungsi melakukan proses komputasi numerik. Sedangkan Array
#  merupakan kumpulan variabel yang memiliki tipe data yang sama. Numpy menyimpan datanya dalam bentuk array.
# Perbedaan antara list dan array adalah fungsi yang dapat Anda lakukan padanya seperti misalnya ketika kita ingin membagi
#  array dengan suatu nilai (misal, 2), hasilnya akan dicetak sesuai permintaan tetapi dalam kasus list, python akan menampilkan
#  pesan error.

import numpy as np  # artinya import numpy sebagai np

a = np.array([1,2,3,4,5])
b = [1,2,3,4,5]  # list biasa gak pake numpy

print(a) # hasilnya kalo numpy array gak ada komanya
print(b) # hasilnya kalo list biasa ada komanya

# perbedaan numpy array dan list
a = a + 1
# b = b + 1  #list biasa tidak bisa seperti ini nanti error
b = b + [1]

print(a)  # kalo numpy array dia akan nambahin semua komponen
print(b)  # kalo ini akan nambahkan 1 di belakannya 