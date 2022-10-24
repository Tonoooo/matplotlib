# sumber : https://youtu.be/u3Ue6IlzbOE
# membuat dan menavigasi di antara beberapa layar. Kami akan melakukan ini 
#menggunakan sesuatu yang disebut ScreenManager.
#jadi kita memiliki beberapa ewindows

from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen # untuk mengatur layar
from screen_nav import screen_helper # mengimport variabel yang berisi buidernya

## membuat class untuk <LayarMenu>, <LayarProfil>, <LayarUpload>
class LayarMenu(Screen):
    pass


class LayarProfil(Screen):
    pass


class LayarUpload(Screen):
    pass


# buat screen manager
sm = ScreenManager() # variabel objek ScreenManager
## masukkan layar-layar nya ke variabel objek ScreenManager,
# layar yang pertama dimasukkan ke screenmanager itu akan menjadi beranda
sm.add_widget(LayarMenu(name='menu'))
sm.add_widget(LayarProfil(name='profile'))
sm.add_widget(LayarUpload(name='upload'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()