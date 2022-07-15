# Sorting NumPy Array
# lanjutannya ada di modul 9Sorting NumPy Array ke2.py dan modul 9Sorting NumPy Array ke3.py

# penjelasan Sorting NumPy Array
# atau link: https://youtu.be/93leimYGXOs

import  numpy as np

# array random(ngacak)
a = np.random.randn(1,6) # ini syntax untuk menjeneret si array random
aa = np.random.randn(1,6)*10 # sirandom nya dikalikan 10
aaa = np.floor(np.random.randn(1,6)*10) # dibulatkan ke bawah

print(aaa)

# mencari nilai tertinggi dan terendah
print('nilai max dari aaa = ',aaa.max()) # mencari nilai tertinggi
print('posisi max dari aaa = ',aaa.argmax()) # argmax = argumen dari nilai tertinggi posisinya ada dimana
print('nilai min dari aaa = ',aaa.min()) # mencari nilai terrendah
print('posisi min dari aaa = ',aaa.argmin()) # argmin = argumen dari nilai terrendah posisinya ada dimana

# mengurutkan
print('mengurutkan nilai aaa = ')
print(np.sort(aaa)) # mengurutkan dari terkecil ke tinggi
print(np.argsort(aaa)) # mengurutkan dari terkecil ke tinggi tapi ditampilkannya pake argumen/index