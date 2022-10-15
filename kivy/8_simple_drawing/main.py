# sumber: https://youtu.be/8vD-V5jpjBo
"""
membuat aplikasi menggambar sederhana menggunakan sesuatu dalam kivy yang disebut canvas.
jadi kita hanya membuat persegi panjang dan itu akan mengikuti mouse disekitar layar
"""

from kivy.app import App
from kivy.uix.widget import Widget # widget ini berfungsi dimana pun seperti gridlayout, floatlayout, dll
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line #  membuat garis.


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch,self).__init__(**kwargs)# artinya kita mengambil init yang ada di super class Widget & kita memasukkan kwargs dan class Touch keparameternya.
        # menggambar persegi panjang
        with self.canvas: # Widget memiliki properti canvas yang bisa kita gunakan
            # untuk mengubah warna objeknya kita harus mengubah warna canvasnya sebelum mengubah warna objeknya
            Color(0, 1, 0, 0.5, mode='rgba') # warna garisnya jadi hijau
            Line(points=(20,30,400,500,60,500)) # membuat garis. points(x , y)
            # untuk perseginya
            Color(1, 0, 0, 0.5, mode='rgba') # mengubah warna perseginya jadi merah. ini rgba
            # ini objek persegi panjang
            self.rect = Rectangle(pos=(0,0), size=(50,50)) # pos = dipojok kiri bawah
            
    
    # overide beberapa method:
    def on_touch_down(self, touch):
        self.rect.pos = touch.pos # mengubaha posisi persegi. saat kita menyentuh layat perseginya akan pergi ke posisi itu
        print("Mouse Down", touch) 

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos # saat mousenya ditekan tahan, perseginya akan mengikuti mouse
        print("Mouse Move", touch)
    # saat ini kita tidak membutuhkan on_touch_up

class MyApp(App):
    def build(self):
        return Touch()
    
if __name__ == "__main__":
    MyApp().run()