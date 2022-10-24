# sumber: https://youtu.be/udjUKJbOaPg
# sumber: https://kivymd.readthedocs.io/en/1.1.1/components/label/#kivymd.uix.label.label.MDLabel.text_color

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon # untuk label dan iconnya
from kivymd.font_definitions import theme_font_styles


class Label(MDApp):
    def build(self):
        ## membuat label
        #membuat variabel label yg berisi label dan tampilan label kita
        label1 = MDLabel(text="Hello world", halign="center", theme_text_color="Error",
                        font_style="Subtitle2")
        ## membuat label dengan warna yang kita inginkan (custom) ditheme_text_color="Custom" pake custom lulu tambahkan parameter text_color=(rgba)
        label2 = MDLabel(text="Hello world", halign="center",theme_text_color="Custom",
                        text_color=(156/255,106/255,184/255,1)) # penjelasan ada dibawah
        ## menampilkan icon
        ikon = MDIcon(icon="language-python", halign="right")
        return label2 # return yang ingin ditampilkan

Label().run() # jalankan aplikasinya

# penjelasan:
"""
posisi teksnya 
halign="center" adalah halign = horizontal align. & center=ditengah.

warna dan tema
theme_text_color="Error" adalah theme_text_color = tema & warnanya teksnya (error=merah)
jika ingin warna teksnya bebas kitabisa tambahkan custom -> theme_text_color="Custom",
setelah itu masukkan warnanya text_color=(r, g, b, a)
di kivymd warna rgb nya tidak menggunakan (255,255,255) tapi meggunakan nila 0 hingga 1, jadi
cara agar nilai 255 menjadi nilai 1 adalah dengan (nilaiwarnanya)/255,(nilaiwarnanya)/255,
(nilaiwarnanya)/255 -> slash / ini artinya dibagi jadi (nilaiwarnaya) dibagi 255
contohnya warna ungu dengan nilai rgb(156, 106, 184) maka menjadi (156/255,106/255,184/255)
jangan lupa dikivymd pake rgba, a = alpha. hasilnya (156/255,106/255,184/255,1)

Styles hurufnya bisa dilihat di link ini:
https://kivymd.readthedocs.io/en/0.104.1/themes/font-definitions/index.html

untuk icon nya ada disini:
https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py
"""