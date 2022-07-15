# Set Label dan Title

import numpy as np
import matplotlib.pyplot as plt

# membuat data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):  # nama fungsi ini disebut cemal case (huruf kecil dikataawal dan kata berikutnya diawali huruf besar). kalo memberi nama class harus diawali huruf besar
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

amplitudo = 1
frekuensi = 1
theta = 0
tAkhir = 4

t,y = sinusGenerator(amplitudo,frekuensi,tAkhir,theta)

# membuat plotnya
plt.plot(t,y)

 # membuat labelnya
judul = 'Grafik Sinusoidal\n'
rumus = r'$ \mathcal{Y} = A.sin(2 \omega t + \theta)$' + '\n' # garismiring(\) disitu untuk menulis simbolnya/style fontnya dan nulisnya didalam si dollarnya dan dollarnya di r ( r artinya raw)
parameter1 = r'$ A = $' + str(amplitudo) + ' cm, ' # r'$ A = $' agar si A nya miring
parameter2 = r'$ \omega = $' + str(frekuensi) + r'$ \mathit{Hz}$' + ', ' # r'$ \omega = $' untuk simbol omega
parameter3 = r'$ \theta = $' + str(theta) + r'$^{o} $'  # r'$^{o} $' untuk derajat

plt.title(judul + rumus + parameter1 + parameter2 + parameter3) # untuk memberi judul
plt.xlabel('waktu (detik)') # labelnya ada dibawah garis x
plt.ylabel('magnetuda(cm)') # labelnya ada disamping garis y

# menampilkan
plt.show()