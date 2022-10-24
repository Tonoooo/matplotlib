# sumber : https://youtu.be/LRXo0juuTrw
# kivymd : https://kivymd.readthedocs.io/

from kivymd.app import MDApp # untuk membuat aplikasinya

# nama class nya sesuai nama aplikasi yang ingin kita buat. tambahkan App(tapi ini bebas)
class CobaApp(MDApp): # meninherit dari MDApp
    def build(self): # mendefisinikan fungsi build (Override Method)
        return

CobaApp().run() # jalankan aplikasinya