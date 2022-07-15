# Set Ticks (Merubah rentang)
# Ticks adalah nilai yang digunakan untuk menunjukkan titik tertentu pada sumbu koordinat. contohnya garis sumbu pada x ada -1 0 1 2.. , pada garis sumbu y ada 0 1 2 3 4 5

import matplotlib.pyplot as plt
import numpy as np

# membuat data
sudut = np.arange(1,360,1) # 1 sampai 360 derajat dengan stepnya 1
y = np.sin(np.deg2rad(sudut))

# membuat plot
plt.plot(sudut,y)
plt.ylabel('magnituda')
plt.xlabel('sudut')

 # mengganti ticks nya
plt.yticks([-1,0,1]) # jadi di garis y cuman ada -1,0,1
plt.xticks([0         ,90         ,180          ,270        ,360], # ini nilainya
           [r'${0}^o$',r'${90}^o$',r'${180}^o$',r'${270}^o$',r'${360}^o$']) # yang ini untuk menambahkan/mengganti agar ada derajatnya. r'${masukkan nilainya disini}^o$'

# menampilkan
plt.show()