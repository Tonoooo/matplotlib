# sumber: https://youtu.be/yg7n8hP6k1w
"""
mendapatkan input pengguna seperti input sentuh dan input dari mouse. Cara 
mendapatkan input ini akan berfungsi di semua perangkat (ponsel, komputer, dll.).
GUI yang sangat sederhana yang terdiri dari satu Tombol. Kita akan menempatkan 
tombol ini di dalam kelas Touch 
"""

from kivy.app import App
from kivy.uix.widget import Widget # widget ini berfungsi dimana pun seperti gridlayout, floatlayout, dll
from kivy.properties import ObjectProperty # ambil variabel dari file kv

# membuat class touch yang menginherit Widget
class Touch(Widget):
    btn = ObjectProperty(None)
    # overide beberapa method:
    #1. ketika menyentuh tombol / Dipicu saat pengguna pertama kali menekan layar.
    def on_touch_down(self, touch):#punya parameter touch = mendapatkan posisi / posisi dimana kita menekan
        print("Mouse Down", touch) # akan memprint posisinya. penjelasan hasilnya ada dibawah
        self.btn.opacity = 0.5 # saat tombol disentuh warnanya akan berubah
    #2. Dipicu ketika pengguna menyentuh layar dan menggerakkan jari atau mouse mereka
    def on_touch_move(self, touch):#
        print("Mouse Move", touch)
    #3. ketika pengguna melepaskan mouse (mengangkat jari nya dari layar)
    def on_touch_up(self, touch): # saat tombol diklik/disentuh 
        print("Mouse Up", touch)
        self.btn.opacity = 1 # saat tombol sentuhannya diangkat warna tombol akan kembali seperti semula

class MyApp(App):
    def build(self):
        return Touch() # return touch agar ditampilkan
    
if __name__ == "__main__":
    MyApp().run()
    
"""
Sekarang jika kita menjalankan program kita, kita akan melihat bahwa input kita 
direkam dan dicetak ke layar. contoh:

Mouse Down <MouseMotionEvent spos=(0.06382978723404255, 0.12020033388981632) pos=(50.99999999999999, 71.99999999999997)>
Mouse Move <MouseMotionEvent spos=(0.20775969962453067, 0.19866444073455758) pos=(166.0, 118.99999999999999)>
Mouse Up <MouseMotionEvent spos=(0.06382978723404255, 0.12020033388981632) pos=(50.99999999999999, 71.99999999999997)>

spos / S posisi = relatif posisi, seperti (pos=(166.0, 118.99999999999999)) absolut posisi
itu memberikan posisi mouse nya
"""