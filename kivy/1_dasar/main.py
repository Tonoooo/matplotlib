# sumber : https://youtu.be/bMHK6NDVlCM

## import
from kivy.app import App # mengimpor class App dari modul app
from kivy.uix.label import Label # mengimpor class Label dari modul label difolder uix

## membuat class
# class ini inherit/mewarisi dari class App yang ada dimodul.
#artinya kita akan mengambil semua properti yang telah ditulis untuk kita dari kivy dari class App
class MyApp(App):# nama classnya bebas.
    # mendefisinikan fungsi build (Override Method)
    #ini akan menjadi antarmuka utama untuk aplikasi kita 
    def build(self):# nama fungsinya harus ini
        # kita ingin menampilkn text maka kita akan mengembalikan Label. memiliki parameter teks 
        return Label(text="Percobaan Pertama") # ini akan menampilkan textnya di window/jendelanya diaplikasi
    
## jalankan 
if __name__ == "__main__": # jika nama file ini adalah file utama(main) maka:
    MyApp().run() # jalankan class MyApp() dan metode run()
    #[metode run() ini bawaan dari class App yang kita inherit. run() akan melakukan semua
    #kofigurasi, akan mengatur semuanya dan menjalankan aplikasi kita]
#MyApp().run() # kita bisa menjalankannya seperti ini tapi disini kita pake
#if __name__ == "__main__": ini berguna jika ada program lain mengimport file ini
#program ini tidak akan menjalankan MyApp().run() karnakan pake if __name.... penjelasan tentaingini https://youtu.be/sYKhxqcDu3w