# sumber : https://youtu.be/M5ztWtJrY24
## Membuat list
# jenis-jenis ada 3 list dikivymd: OneLineListItem, TwoLineListItem, ThreeLineListItem
#OneLineListItem = berisi 1 baris teks saja, TwoLineListItem = berisi 2 baris teks
#ThreeLineListItem = berisi 3 baris teks

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
#MDList=agar si item listnya tidak tumpang tindih/nimpa satu sama lain, agar berjajar berurutan
from kivy.uix.scrollview import ScrollView # agar listnya bisa discroll

class DemoApp(MDApp):
    def build(self):
        screen = MDScreen() # buat variabel objek screen
        ## membuat simpel list
        scroll = ScrollView() # agar listnya bisa discroll, buat variabel objek ScrollView()
        list_view = MDList() # buat variabel objek MDList. ini akan berisi item listnya
        ## membuat 20 item list menggunakan for loop
        for i in range(20):
            # buat variabel objek ThreeLineListItem untuk listnya. contoh penggunaan OneLineListItem dll ada dibawah
            items = ThreeLineListItem(text=str(i) + ' item', # str(i) = karna i bertipe int ubah jadi str
                                     secondary_text='This is ' + str(i) + 'th item',
                                     tertiary_text='hello')
            list_view.add_widget(items) # masukkan item listnya ke variabel objek (list_view)
        ## masukkan list yang berisi item-itemnya ke scroll agar bisa discroll
        scroll.add_widget(list_view) 
        # End List
        ## terakhir masukkan scroll yang berisi list ke variabel objek screen
        screen.add_widget(scroll)
        return screen

DemoApp().run()

"""
~ contoh penggunaan OneLineListItem:
item = OneLineListItem(text='apa aja')

~ contoh penggunaan TwoLineListItem:
item = TwoLineListItem(text='judul', secondary_text='apapun')

~ contoh penggunaan ThreeLineListItem:
items = ThreeLineListItem(text='judul', secondary_text='aaaaa', tertiary_text='bbbbb')

aliran proses membuat list = 
OneLineListItem(tentukan&buatitemlist) -> masukkan ke MDList -> masukkan ke ScrollView -> masukkan ke Screen
"""

# lanjut di 9_avatar&icon_list