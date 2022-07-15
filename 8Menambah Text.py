# Menambah Text

import numpy as np
import matplotlib.pyplot as plt

# membuat data(sin(2wt + theta))
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):  # nama fungsi ini disebut cemal case (huruf kecil dikataawal dan kata berikutnya diawali huruf besar). kalo memberi nama class harus diawali huruf besar
    t = np.arange(0,tAkhir,0.1)
    y = amplitudo * np.sin(2*frekuensi * t + np.deg2rad(theta))
    return t,y

t,y = sinusGenerator(1,1,4,0) # jadi t,y artinya variabel t dan y keduanya sama memiliki sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t,y)
 # cara membuat textnya: plt.text(bebasposisi di x, bebasposisi di y, "disini text nya")
plt.text(2,0.5, r'$ y = \mathcal{A}.sin(2 \omega t)$')
plt.text(2,0.4, r'$ \mathcal{A} = 1 cm, \omega = 1 Hz$')

# menampilkan
plt.show()