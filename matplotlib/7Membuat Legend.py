# Membuat Legend
# fungsi legend untuk memberi tahu grafik tersebut untuk apa

import numpy as np
import matplotlib.pyplot as plt

# membuat data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):  # nama fungsi ini disebut cemal case (huruf kecil dikataawal dan kata berikutnya diawali huruf besar). kalo memberi nama class harus diawali huruf besar
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)
t2,y2 = sinusGenerator(1,1,4,90)

# membuat plotnya
"""
# tipe pertama
plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
plt.legend() # stelah nulis nama labelnya (contohnya: label='sin(0)') lalu tulis plt.legend() agar bisa dihasilkan
"""
"""
# tipe kedua
plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')# stelah nulis nama labelnya (label='sin(0/90)') lalu tulis plt.legend() agar bisa dihasilkan
plt.legend(loc="upper center") # loc="" artinya untuk menentukan lokasi legend nya ada di mana
"""
"""
# tipe ketiga
plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
plt.legend(loc="upper center", bbox_to_anchor=(0.5,-0.05)) # bbox_to_anchor=(0.5,-0.05) si legend nya ada diluar dan 0.5 itu x, -0.05 itu y
"""
# tipe keempat
plt.figure(1) # ini si figure nya (nantikan kalau dirun ada hasil nya tah nanti sihasilnya itu)
ax = plt.subplot(111) # subplot itu kotak yang didalamnya ada grafik
plt.plot(t1,y1, label='sin(0)')
plt.plot(t2,y2, label='sin(90)')
box = ax.get_position() # untuk mendapatkan posisi subplot(subplot/kotak yang didalamnya ada grafik)
ax.set_position([box.x0, box.y0, box.width*0.7, box.height]) # menentukan posisi subplot(subplot/kotak yang didalamnya ada grafik)
plt.legend(loc="upper center", bbox_to_anchor=(1.2,1))

# menampilkan
plt.show()