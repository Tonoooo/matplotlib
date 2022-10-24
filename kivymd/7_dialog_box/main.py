# sumber : https://youtu.be/GO62UFvyyns
# Ini menlanjutkan dari sebelumnya (6_binding_input_tombol).
## Menampilkan input user ke dialog box

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import username_input # mengambil variabel yang berisi bahasa desain kv untuk text field
from kivymd.uix.dialog import MDDialog # untuk dialog boxnya
from kivymd.uix.button import MDFlatButton

# variabel username_input yang berisi bahasa desain kv ada difile helpers.py
#disini hanya perlu menimport nya saja.

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette="Green"# warna tema elemennya hijau
        screen = MDScreen()
        ## memuat builder pada variabel username_input. 
        self.username = Builder.load_string(username_input)
        button = MDRectangleFlatButton(text='Tampilkan',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.35},
                                       on_release=self.show_data) 
        
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen
    ## fungsi untuk menampilkan input user di dialog
    def show_data(self, obj):
        ## logika if untuk isi dialognya
        if self.username.text is not "": # jika input user tidak kosong maka:
            isi_dialognya = self.username.text + " itu yg anda ketikan."
        else: # tapi jika user tidak memasukkan input maka:
            isi_dialognya = "Tolong masukkan user name"
        ## membuat tombol tutup dialog dan tombol more pada dialognya
        tutup_dialog = MDFlatButton(text='Tutup', on_release=self.close_dialog) # aksinya ada difungsi close_dialog
        tombol_more = MDFlatButton(text='More')
        ## membuat objek dialog. 
        self.dialog = MDDialog(title='Username check', # untuk judul dialog
                               text=isi_dialognya, # teks isi dialog
                               size_hint=(0.8, 1), # ukuran dialognya
                               # menambahkan tombol didialognya. masukkan diparameter buttons, ini bertipe list, jadi bisa memasukkan banyak tombol
                               buttons=[tutup_dialog,tombol_more])
        self.dialog.open() # buka dialog. jadi jika ada yg manggil fungsi show_data ini, maka akan muncul dialog
    ## fungsi untuk menutup diaolog. ini aksi dari tombol tutup didialog
    def close_dialog(self, obj):
        self.dialog.dismiss() # tutup dialog
        # lakukan hal-hal setelah menutup dialog

DemoApp().run()
