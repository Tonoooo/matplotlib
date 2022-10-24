# sumber : https://youtu.be/6uGZfBTl8Xc

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField # untuk membuat textfieldnya. tapi jika kita 
#menggunakan builder method tidak usah meninport MDTextField
from kivy.lang import Builder

## membuat textfield menggunakan method builder. ini sama dengan bahasa desain kv
# pake multiline string
username_input = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:180
"""
#didalam multiline string itu, masukkan elemen/komponen yang kita inginkan, disana pake MDTextField
# MDTextField: ini otomatis menimport MDTextField didalam pythone code, jadi kita tidak perlu import MDTextField lagi
#lalu masukkan atribut yang kita ingin kan. 
#hint_text = memberikan petunjuk diatas input. helper_text = petunjuk dibawah input
#helper_text_mode = ada 2 mode: persistent teksnyaterus menerus akan ditampilkan dilayar & on_focus
#teksnya akan tampil saat kita mengklik inputnya.
#icon_right = ikon yang berada disamping kanan input. icon_right_color = warna icon
#pos_hint = posisi TextField. size_hint_x:None = panjang lebarnya tetap. width:200 = lebar 200

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"# warna tema elemennya hijau
        screen = MDScreen()
        
        ## membuat textfieldnya dengancara dipython langsung
        # username = MDTextField(
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     size_hint_x=None, width=200) # penjelasan dibawah
        ## membuat textfieldnya dengancara dimthode builder. disini hanya perlu memuat builder kemudian
        # masukkan variabel multiline string yang berisi desaintampilan textfieldnya yg diatas
        username = Builder.load_string(username_input) # jadi variabel ini berbentuk objek yang mengandung textfield
        screen.add_widget(username)
        return screen

DemoApp().run()

# size_hint
#memiliki 2 nilai: x = lebar & dan y = tinggi. untuk nilainya dari 0 sampai 1
#1 = 100%, jika 0.5 = 50%.. contoh size_hint=(0.5,0.5) maka lebar dan tingginya
#50% sesuang dengan layarnya. jika layarnya mengecil ukuran ini pun ikut mengecil
# size_hint_x=None, width=200)
#size_hint_x=None artinya lebarnya tetap, mau layarnya mengecil sekalipun lebarnya
#tidak akan berubah. width=200 lebarnya 200
## lanjut di 6_binding_input_tombol