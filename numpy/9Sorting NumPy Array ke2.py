# Sorting NumPy Array ke 2

import  numpy as np

# array random(ngacak)
a = np.floor(np.random.randn(2,2)*10) # 2 baris 2 kolom dan setiap komponen dikali 10
print(a)

# mencari nilai tertinggi dan terendah
print('nilai max dari aaa = ',a.max()) # mencari nilai tertinggi
print('posisi max dari aaa = ',a.argmax()) # argmax = argumen dari nilai tertinggi posisinya ada dimana
print('nilai min dari aaa = ',a.min()) # mencari nilai terrendah
print('posisi min dari aaa = ',a.argmin()) # argmin = argumen dari nilai terrendah posisinya ada dimana

# mengurutkan
print('mengurutkan nilai aaa = ')
print(np.sort(a)) # mengurutkan dari terkecil ke tinggi
print(np.argsort(a)) # mengurutkan dari terkecil ke tinggi dan diurutkannya perbaris tapi ditampilkannya pake argumen/index