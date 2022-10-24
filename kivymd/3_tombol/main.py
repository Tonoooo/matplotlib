# sumber: https://youtu.be/YUwd4TMXc88

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen # ini seperti gridlayout dikivy untuk tata letak
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class TombolApp(MDApp):
    def build(self):
        screen = MDScreen() # membuat objek dari Screen, dan ini akan menjadi tempat menyimpan/menampilkan elemen elemen kita.untuk namanya bebas
        ## membuat tombol (tidak menampakkan border)
        btn_flat = MDFlatButton(text='Tombol flat', pos_hint={'center_x': 0.25, 'center_y': 0.5})
        screen.add_widget(btn_flat) # masukkan ke layar
        ## membuat tombol yang menampakkan border
        btn_persegipjg = MDRectangleFlatButton(text='Persegi panjang', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_persegipjg) # masukkan ke layar
        ## tombol icon
        icon_btn = MDIconButton(icon="beaker-question",pos_hint={'center_x': 0.75, 'center_y': 0.5})
        screen.add_widget(icon_btn) # masukkan ke layar
        ## membuat tombol yang menampakkan padding/area yang berwarna, berisi ikon, dan tombolnya seperti mengambang
        btn = MDFloatingActionButton(icon="android",
                                     pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                     )
        screen.add_widget(btn) # masukkan ke layar
        return screen


TombolApp().run()


# untuk icon nya ada disini:
# https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py