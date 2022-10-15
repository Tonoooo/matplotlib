# sumber: https://www.youtube.com/watch?v=AS3b70pLYEU&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=4

### membuat app yang sama dengan app sebelumnya namun disini kita akan pake .kv

"""
Bahasa Desain kv
Sampai saat ini kami telah menambahkan widget ke jendela/aplikasi kami menggunakan kode python.
Ini dapat diterima dan berfungsi dengan baik namun ada cara yang jauh lebih mudah dan lebih baik
untuk melakukan ini.
Kivy memiliki sesuatu yang disebut bahasa desain kv. Anda menganggapnya sebagai bahasa yang mirip
dengan HTML dan CSS di mana ia bertanggung jawab untuk menata dan menambahkan elemen ke tampilan
tetapi tidak menangani logika apa pun. Dalam tutorial ini saya akan menunjukkan cara membuat 
file .kv dan membuat bagian grafis aplikasi Anda dari dalam file itu.

Catatan: Kami masih membutuhkan skrip python untuk menangani logika dan memuat aplikasi.

Penamaan : Nama file .kv Anda harus mengikuti aturan di bawah ini agar python/kivy dapat melihat
dan memuat file tersebut.
1. Harus huruf kecil semua
2. Harus sesuai dengan nama kelas utama Anda. (Yang memiliki metode build)
3. Jika nama kelas utama Anda diakhiri dengan "app" (huruf kecil atau besar), Anda tidak boleh menyertakan "app" dalam nama file Anda.

Lokasi File: File harus berada di direktori yang sama dengan skrip python Anda.
Ekstensi File: File harus disimpan sebagai tipe *Semua File dan diakhiri dengan .kv
Sebagai contoh:
Nama kelas utama saya adalah MyApp . Oleh karena itu saya akan menamai file saya my.kv .
"""

from kivy.app import App
# karna kita akan menggunakan kv file kita harus import widget
from kivy.uix.widget import Widget

"""_
Hal pertama yang perlu kita lakukan untuk menambahkan widget ke layar kita menggunakan .kv 
adalah menyiapkan kelas kosong di skrip python kita. Kelas ini hanya akan mewarisi dari Widget 
dan akan digunakan dari dalam file kv untuk menambahkan widget.
"""
class Gridaku(Widget):#inherit dari class Widget. 
    pass


class MyApp(App): # <- Main Class
    def build(self):
        return Gridaku()


if __name__ == "__main__":
    MyApp().run()
    
# lanjutannya di bagian 5.