# sumber : https://www.folkstalk.com/2022/09/kivymd-navigation-with-code-examples.html
## Menggunakan Laci Navigasi untuk Mengubah Layar

from kivymd.app import MDApp
from kivy.lang.builder import Builder

class Main(MDApp):
    def build(self):
        screen = Builder.load_file("layout.kv")
        return screen
    ## untuk fungsi aksi saat user mengklik card yang ada dihalaman quiz
    def aa(self, cardbrp):
        print(f"anda menklik {cardbrp}")
Main().run()