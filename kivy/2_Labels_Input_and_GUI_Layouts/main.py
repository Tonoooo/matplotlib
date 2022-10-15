# sumber : https://youtu.be/QUHnJrFouv8

from cgitb import text
from kivy.app import App # mengimpor class App dari modul app
from kivy.uix.label import Label # mengimpor class Label dari modul label difolder uix
## import lainnya
from kivy.uix.gridlayout import GridLayout # mengimport class GridLayout untuk tata letak grid
from kivy.uix.textinput import TextInput # mengimport class TextInput untuk memasukkan text

### disini kitakan membuat aplikasi kecil pertama kita hanyalah untuk menanyakan nama dan email

## membuat class yang akan menampun semua elemen desain kita
#menggambar sesuatu ke layar
class GridAku(GridLayout):# nama classnya bebas. ini menginherit dari GridLayout
    # membuat inisialisasi
    def __init__(self, **kwargs): # pake kwargs agar bisa menampung argumen banyak
        super(GridAku, self).__init__(**kwargs)# artinya kita mengambil init yang ada di super class (GridLayout) & kita memasukkan kwargs keparameternya.
        ### mengubah properti yang dimiliki GridLayout
        self.cols = 2 # kita akan memiliki 2 kolom
        ## menambahkan widget label
        self.add_widget(Label(text="Nama Pertama: ")) # kita menggunakan metode dari GridLayout untuk membuat widget label teks
        ## menambahkan widgt input teks
        self.nama1 = TextInput(multiline=False) # karena secara default memiliki beberapa baris dikotak input teks kita,tetapi kita hanya ingin 1
        #maksudnya ketikan kita mengetikkan banyak teks, teks tersebut akan disatu baris saja. tidak akan kebawah/baris baru
        self.add_widget(self.nama1) # memasukkan  input teks yang diatas tadi kelayar
        
        self.add_widget(Label(text="Nama terakhir: "))
        self.nama2 = TextInput(multiline=False)
        self.add_widget(self.nama2)
        
        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

## membuat class utama
class MyApp(App):# nama classnya bebas.
    def build(self):# namanya harus ini.
        return GridAku() # mereturn class GridAku() karna ketika kita meninherit GridLayout keclss GridAku
                        # kita mendapatkan properti grid/kisi,tinggi,kolom,widget Jadi ketika kita 
                        #mereturn class GridAku dimethod build ini kita benarbenar menggambar semua
                        #widgetdan semua grid yang kita miliki ke app(aplikasi) kita

## jalankan 
if __name__ == "__main__":
    MyApp().run()