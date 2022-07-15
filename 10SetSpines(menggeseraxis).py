# Set Spines (menggeser axis)
# mengatur posisi axis di plotnya

import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(1,360,1) # 1 sampai 360 derajat dengan stepnya 1
y = np.sin(np.deg2rad(sudut))

# membuat plot
plt.plot(sudut,y)
plt.title("grafik sinusoidal")
plt.text(190,1,'magnituda')
plt.text(360,0.1,'sudut')

plt.yticks([-1,-0.5,0,0.5,1])
plt.xticks([0         ,90         ,180          ,270        ,360],
           [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$'])

 # menggeser axis
ax = plt.gca() # gca(get caren axis)
ax.spines['left'].set_position(('data',180)) # spines['left'] itu garis yang kiri (yang y). posisinya didata ke 180 (tepatnya garis di x yang ke 180 jadi ditengah)
ax.spines['bottom'].set_position(('data',0)) # garis yang dibawah posisinya mengikuti data ke o (posisi garis nya ada di y ke 0)
ax.spines['right'].set_color('none') # jaadi garis yang kanan gak ada
ax.spines['top'].set_color('none') # garis yang atas gak ada

# menampilkan
plt.show()