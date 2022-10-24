from kivymd.app import MDApp
from kivy.lang.builder import Builder

class Praktek(MDApp):
    def build(self):
        self.icon = "logosquidward.png" # logo aplikasinya. format png, ukuran 256,256
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_file("layout.kv")
        return screen
    # fungsi untuk pindah layar
    def change_screen(self, screen):
        self.root.ids.layar.current = screen
    
Praktek().run()