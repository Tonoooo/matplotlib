from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget

list_helper = """
MDScreen:
    ScrollView:
        MDList:
            id: container
            
"""
# di dalam MDList kita masukkan id dan id itu bernama container (namanya bebas)
#berfungsi untuk menandakan, ini kita gunakan untuk meloop item list di code python

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper) # muat builder
        return screen
    ## kita akan overide method, fungsi ini akan dipanggil setiap kali aplikasi kita
    #dimulai, makanya namanya on_start
    def on_start(self):
        # disini kita for loop untuk isi/item list nya sebanyak 20 buah
        for i in range(20):
            icon = IconLeftWidget(icon="car") # muat ikon nya
            item = OneLineIconListItem(text='Item ' + str(i)) # kita pake OneLineListItem
            item.add_widget(icon) # tambahkan ke item list kita
            # setelah itemnya dibuat, lalu kita masukkan ke MDList yang ada di builder
            self.root.ids.container.add_widget(item) # menambahkan item tadi ke id container
            # self=siaplikasinya, root=sibuilder, ids=kita merujuk ke id, container nama id,
            #add_widget(item) = menambahkan item list kita
    # Ada juga fungsi selain on_start yaitu on_stop=saat kita menutup aplikasinya fungsi ini akan dipanggil
    #,selain itu ada juga yang lainnya....

DemoApp().run()