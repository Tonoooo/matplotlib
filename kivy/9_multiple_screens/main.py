# sumber : https://youtu.be/xaYn4XdieCs
# membuat dan menavigasi di antara beberapa layar. Kami akan melakukan ini 
#menggunakan sesuatu yang disebut ScreenManager.
#jadi kita memiliki beberapa ewindows dan kemudian melakukan transisi

from kivy.app import App
from kivy.lang import Builder # untuk memuat file kv
"""Untuk contoh ini saya akan menggunakan formulir login standar yang mirip dengan yang
telah kita buat sebelumnya. Satu jendela akan menjadi formulir login dan yang lainnya
hanya akan memiliki tombol yang memungkinkan kita untuk menavigasi kembali ke formulir."""
from kivy.uix.screenmanager import ScreenManager, Screen # untuk mengatur layar

"""Untuk setiap jendela yang ingin kita buat, kita perlu membuat kelas kosong yang
mewarisi dari kelas Screen. Jika kita akan bekerja dengan lebih dari satu jendela 
maka kita perlu membuat kelas yang akan mengelola navigasi antara jendela ini. 
Kelas ini perlu mewarisi dari ScreenManager. untuk nama class nya gak harus sama, yang penting kita ngerti"""
class MainWindow(Screen): # layar / halaman utama. ini akan menjadi halaman formulir login
    pass


class SecondWindow(Screen): # halaman kedua
    pass

# jika ingin menambah layar/halaman lain, tinggal tambah lagi

class WindowManager(ScreenManager): # ini akan mewakili/mengatur seperti transisi dll diantara layat
    pass

"""Kivy memiliki sesuatu yang disebut Builder yang memungkinkan kita untuk langsung
memuat file kv apa pun yang kita inginkan. Ini memungkinkan kita untuk menghindari 
penggunaan konvensi penamaan aneh yang harus kita ikuti sebelumnya."""
kv = Builder.load_file('inifile.kv') # memuat file kv kita

class MyMainApp(App):
    def build(self):
        return kv# mereturn variabel kv yang diatas


if __name__ == "__main__":
    MyMainApp().run()