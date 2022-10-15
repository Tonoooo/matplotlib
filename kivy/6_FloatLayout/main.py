# sumber : https://youtu.be/lnOTAq4NQfQ
#Sama seperti kita menggunakan GridLayout di tutorial sebelumnya, kita akan menggunakan FloatLayout
#untuk menyimpan dan menempatkan widget kita.
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout # impoer FloatLayout
#FloatLayout memungkinkan kita untuk menempatkan elemen menggunakan sesuatu yang disebut posisi 
#relatif. Ini berarti bahwa alih-alih mendefinisikan koordinat tertentu, kami akan menempatkan 
#semuanya menggunakan persentase atau berdasarkan lebar dan tinggi jendela saat ini. Dengan cara 
#ini ketika kita mengubah dimensi jendela semua yang telah kita tempatkan akan menyesuaikan ukuran 
#dan posisi yang sesuai dengan skala aplikasi kita dengan ukuran jendela.

class MyApp(App):
    def build(self):
        return FloatLayout() # mengembalikan FloatLayout. karna kita akan bermain di file .kv
    
if __name__ == "__main__":
    MyApp().run()