# Indexing, Slicing dan Iterasi

import numpy as np

a = np.arange(10)**2 # 1 sampai sebelum 10 tapi dipangkat 2

print(a)

# mengambil nilai (Indexing)
print('elemen ke 1 dari a adalah', a[0]) # [0] artinya index ke 0 (index dimulai dari 0)
print('elemen ke 7 dari a adalah', a[6])
print('elemen akhir dari a adalah', a[-1]) # [-1] artinya index terakhir

# slicing rentan dari array
print('elemen ke 1 sampai 6 adalah', a[0:6]) #[0:6] artinya [mulai,selesai], yang terakhir tidak akan dimasukkan, jadi index 0 samppai sebelum 6
print('elemen dari 4 sampai akhir adalah', a[3:]) # [3:] artinya dari index 3 sampai akhir
print('elemen dari awal sampai 5 adalah', a[:5]) #[:5] artinya dari awal sampai sebelum index 5

# iterasi
for i in a:
    print('value = ',i)
