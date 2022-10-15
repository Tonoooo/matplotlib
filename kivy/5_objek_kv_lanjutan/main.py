# sumber: https://youtu.be/H8aWfu9aICc

""" 
Properti Objek
Setelah bereksperimen dengan bahasa .kv, beberapa dari Anda mungkin bertanya: Bagaimana kami 
mengakses elemen kami (textinput, tombol, dll.) dari skrip python kami? Itu adalah pertanyaan yang
bagus dan untuk apa kita memiliki properti objek!
Properti objek memungkinkan kita untuk membuat referensi ke widget dari dalam file .kv dari skrip
python kita.
"""

from kivy.app import App
from kivy.uix.widget import Widget
# untuk menggunakan properti objek dari dalam skrip python adalah mengimpor modul tertentu.
from kivy.properties import ObjectProperty

class Gridaku(Widget):#inherit dari class Widget.
    # mengakses data dari file kv. objek properti
    nama = ObjectProperty(None) # penamaan variabelnya harus sama dengan yang difile kv
    email = ObjectProperty(None)
    """ None = Kami menginisialisasi nilai-nilai sebagai Tidak Ada untuk memulai karena ketika kami pertama
    kali membuat kelas mereka tidak akan memiliki nilai. Sekarang jika kita ingin mengakses nilai 
    kotak TextInput dengan id email kita cukup menggunakan self.email untuk melakukannya. Kemiripan untuk nama TextInput."""
    
    # fungsi yang dipanggil ketika tombol ditekan
    def btn(self):
        print(f"Namanya = {self.nama.text} Emailnya = {self.email.text}")
        self.nama.text = ""# Atur ulang teks menjadi kosong di setiap input teks 
        self.email.text = ""


class MyApp(App): # <- Main Class
    def build(self):
        return Gridaku()


if __name__ == "__main__":
    MyApp().run()