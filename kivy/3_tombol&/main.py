# sumber : https://youtu.be/fGWHQA3LhJ8

from cgitb import text
from kivy.app import App # mengimpor class App dari modul app
from kivy.uix.label import Label # mengimpor class Label dari modul label difolder uix
from kivy.uix.gridlayout import GridLayout # mengimport class GridLayout untuk tata letak grid
from kivy.uix.textinput import TextInput # mengimport class TextInput untuk memasukkan text
## import lainnya
from kivy.uix.button import Button

"""
>>> Multiple Layouts
membuat beberapa tata letak kisi .
Kita dapat menambahkan semua label dan kotak input teks ke dalam tata letak dengan dua kolom dan 
kemudian menambahkan tata letak itu ke tata letak lain yang hanya berisi satu kolom. Kami juga 
akan menambahkan tombol kami ke dalam tata letak dengan hanya satu kolom sehingga mencakup seluruh
bagian bawah layar. Pada dasarnya kita akan menggunakan dua tata letak kotak dan menempatkan satu
di dalam yang lain.
"""

class GridAku(GridLayout):# nama classnya bebas. ini menginherit dari GridLayout
    # membuat inisialisasi
    def __init__(self, **kwargs):
        super(GridAku, self).__init__(**kwargs)
        self.cols = 1 # layout utama hanya memiliki 1 kolom
        
        ### layout yang ada didalam layout utama. layout input. posisi layout ini akan ada diatas
        # Buat tata letak grid baru 
        self.inside = GridLayout() # membuat objek dari class GridLayout. inilah yang mengandung semua widget label&inputnya
        self.inside.cols = 2 # dilayout ini kita memiliki 2 kolom
        
        self.inside.add_widget(Label(text="Nama Pertama: ")) 
        self.nama1 = TextInput(multiline=False)
        self.inside.add_widget(self.nama1)
        
        self.inside.add_widget(Label(text="Nama terakhir: "))
        self.nama2 = TextInput(multiline=False)
        self.inside.add_widget(self.nama2)
        
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        # memasukkan layout ini (yang diatas) ke layout utama. jika tidak ini tidak akan ditampilkan
        self.add_widget(self.inside) 
        
        ### layout utama.
        ## posisi tombol akan dibawah layout input
        self.submit = Button(text="Submit",font_size=40)# submit merupakan nama tombol kita. bebas
        # Kita akan mengikat tombol ke fungsi/metode yang kita buat sehingga ketika tombol itu diklik fungsi tersebut akan berjalan.bind()
        self.submit.bind(on_press=self.pressed)# pressed adalah nama metode yang ingin kita jalankan 
        self.add_widget(self.submit)#masukkan tombol submit ke widget / layout utama
        
    # fungsi yang dipanggil ketika tombol ditekan
    def pressed(self, instance):
        # mengakses teks dari 
        fnama = self.nama1.text # nama pertama
        lnama = self.nama2.text # nama kedua
        email = self.email.text 
        print(f"Nama: {fnama}, last name: {lnama}, email: {email}")
        
        # Atur ulang teks menjadi kosong di setiap input teks 
        self.nama1.text = ""
        self.nama2.text = ""
        self.email.text = ""
        #Jika kita menjalankan program dan mengklik tombol, kita akan melihat bahwa input teks dihapus dan input kita dicetak ke konsol.


## membuat class utama
class MyApp(App):# nama classnya bebas.
    def build(self):# namanya harus ini.
        return GridAku()

## jalankan 
if __name__ == "__main__":
    MyApp().run()