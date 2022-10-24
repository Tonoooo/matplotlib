# sumber : https://youtu.be/VqLpDaTRGLo
# Ini menlanjutkan dari sebelumnya (5_text_field).
## Mengambil input user yang di textfield, kita akan mengikat inputan tadi
#dengan tombol kita, jadi setiap kita mengklik tombol, itu akan menampilkan 
#text input ke terminal, itu disebut binding

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton # tombol persegi panjang
from kivy.lang import Builder
from helpers import username_input # mengambil variabel yang berisi bahasa desain kv untuk text field

# variabel username_input yang berisi bahasa desain kv ada difile helpers.py
#disini hanya perlu menimport nya saja.

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"# warna tema elemennya hijau
        screen = MDScreen()
        ## memuat builder pada variabel username_input. 
        self.username = Builder.load_string(username_input) # jadi variabel ini berbentuk objek yang mengandung textfield 
        #divariabelnya pake self agar si variabel objek username bisa diakses diluar fungsi ini
        ## buat tombol persegi panjang
        button = MDRectangleFlatButton(text='Tampilkan',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.35},
                                       on_release=self.show_data) 
        #untuk aksi tombolnya pake on_release. self.show_data = self adalah aplikasinya, show_data adalah memanggil fungsi show_data.
        #itu pake self karna fungsi show_data berada diluar fungsi build ini.
        
        screen.add_widget(self.username) # pake self
        screen.add_widget(button)
        return screen

    def show_data(self,obj): # obj = parameter objek, ini dibutuhkan oleh kivymd
        # menampilkan input user ke terminal
        print(self.username.text) # self.username.text untuk mendapatkan input textnya
        # ingat variabel username adalah objek text field.

DemoApp().run()

## lanjut di 7_dialog_box