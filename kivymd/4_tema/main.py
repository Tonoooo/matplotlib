from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton


class TemaApp(MDApp):

    def build(self): # self ini mengacu pada aplikasi yang kita buat
        # kita ingin mengubah tema aplikasi maka itu akan akan merujuk ke self. maka kita ubah tema si self itu
        # mengubah warna tema elemen elemen aplikasinya. Semua komponen material utama akan memiliki warna tema warna yang ditentukan.
        self.theme_cls.primary_palette = "Orange" # maka tombol, navigasi, topbar dan komponen lainnya memiliki warna oren
        # mengubah seberapa cerah atau gelapnya ini disebut hue
        self.theme_cls.primary_hue = "100"
        # tema later belakangnya. pilih Dark atau Light
        self.theme_cls.theme_style = "Dark"

        ## sebagi contoh disini kita masukkan tombol persegi panjang
        screen = MDScreen()
        btn_flat = MDRectangleFlatButton(text='Hello World',
                                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_flat)
        return screen

TemaApp().run()

""" Penjelasan:
~ What is a theme?
settiap kali kita memberi warna yang perlu diterapkan ke semua elemen dalam aplikasi kita, 
itu disebut tema. misal kita beri warna temanya hijau maka tombol, navigasi, topbar dan semua 
elemen lainnya akan memiliki warna yang sama

self.theme_cls.primary_palette
self = self ini mengacu pada aplikasi yang kita buat
theme_cls = kita akan megubah tema nya
primary_palette = Semua komponen material utama akan memiliki warna tema warna yang ditentukan.
Jadi misal kita pilih primary_palette = "Green" maka warna tombol, navigasi, topbar semua 
elemen memiliki warn hijau

nah untuk pilihan warna di primary_palette - Available options are:
‘Red’, ‘Pink’, ‘Purple’, ‘DeepPurple’, ‘Indigo’, ‘Blue’, ‘LightBlue’, ‘Cyan’, ‘Teal’, ‘Green’, ‘LightGreen’, ‘Lime’, ‘Yellow’, ‘Amber’, ‘Orange’, ‘DeepOrange’, ‘Brown’, ‘Gray’, ‘BlueGray’.
lihat di: https://kivymd.readthedocs.io/en/1.1.1/themes/color-definitions/

tingkat kecerahan warnanya disebut Primary hue. self.theme_cls.primary_hue 
pilihan - ‘50’, ‘100’, ‘200’, ‘300’, ‘400’, ‘500’, ‘600’, ‘700’, ‘800’, ‘900’, ‘A100’, ‘A200’, ‘A400’, ‘A700’.
lihat di: https://kivymd.readthedocs.io/en/1.1.1/themes/color-definitions/

self.theme_cls.theme_style 
theme_style = atau tema latar belakangnya memiliki dua pilihan
Dark or Light

~ kesimpulan
untuk tema warna latarbelakang di self.theme_cls.theme_style , untuk tema para 
komponennya self.theme_cls.primary_palette , untuk tingkat kecerahan warnanya
self.theme_cls.primary_hue
"""