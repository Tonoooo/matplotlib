# sumber : https://youtu.be/K37fAl6u2uM
# ini lanjutan dari 8_list
## memasukkan avatar(gambar) atau icon ke list item
# untuk list yang memiliki bericon/avatar pakenya bukan OneLineListItem tapi
#pake OneLineIconListItem (ditambah icon) untuk yang avatar pake OneLineAvatarListItem
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList
## import untuk list bericon/beravatar(gambar)
# ini untuk list bericon
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem, ThreeLineIconListItem # pilih salahsatu mau yang berapa baris
# ini untuk list beravatar (pake gambar kita sendiri)
from kivymd.uix.list import OneLineAvatarListItem, TwoLineAvatarListItem, ThreeLineAvatarListItem # pilih salahsatu mau yang berapa baris
## import terakhir untuk si icon berada di kanan atau dikiri. untuk icon pake IconLeftWidget/IconRightWidget
#kalau gambar pake ImageLeftWidget/ImageRightWidget
from kivymd.uix.list import IconLeftWidget, ImageLeftWidget

class DemoApp(MDApp):
    def build(self):
        screen = MDScreen()
        
        scroll = ScrollView()
        list_view = MDList()
        ## membuat 20 item list menggunakan for loop
        for i in range(20):
            ## untuk menambahkan icon/avatar buat variabel untuk nampungnya
            gambar = ImageLeftWidget(source="images.jpg")
            # buat variabel objek ThreeLineListItem untuk listnya. contoh penggunaan OneLineListItem dll ada dibawah
            items = ThreeLineAvatarListItem(text=str(i) + ' item', # str(i) = karna i bertipe int ubah jadi str
                                     secondary_text='This is ' + str(i) + 'th item',
                                     tertiary_text='hello')
            items.add_widget(gambar) # memasukkan si icon / avatar nya ke item list
            list_view.add_widget(items)
            
        scroll.add_widget(list_view) 
        ## terakhir masukkan scroll yang berisi list ke variabel objek screen
        screen.add_widget(scroll)
        return screen

DemoApp().run()