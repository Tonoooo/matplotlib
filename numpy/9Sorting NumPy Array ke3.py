# Sorting NumPy Array ke3

import numpy as np

dtipenya = [('nama','S10'),('tinggi',int)] # ('nama','S255'),('tinggi',int) ini seperti argumen difungsi dana S10 = s artinya string dan 210 adalah batasnya sampai 210(bebas sihh batas nya mauberapaaja)
data = [
    ('tono',180),
    ('suep',170),
    ('taat',175)
]

a = np.array(data,dtype=dtipenya)
print(a)

# mengurutkan
print(np.sort(a, order='tinggi')) # mengurutkan a menurut tingginya dari yang terkecil ke tinggi
print(np.sort(a, order='nama'))  # mengurutkan a menurut namanya sesuai abjad