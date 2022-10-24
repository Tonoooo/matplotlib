# sumber : https://youtu.be/iicfEqNBb-4
# tool bar ada 2 jenis: atas dan bawah. difile ini untuk toolbar atas.
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window # ini untuk windownya

Window.size = (300, 500) # piksel. mengubah ukuran window aplikasinya 
#INGAT KITA DISINI MENETAPKAN UKURAN WINDOW hanya untuk saat MEMBUAT APLIKASI SAJA
#agar saat programnya dirun tidak usah mengecilkan windownya.
#JANGAN MENETAPKAN UKURAN WINDOW NYA SAAT MENGCOMPAIL APKNYA

screen_helper = """
MDScreen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["car", lambda x: app.navigation_draw()]]
            elevation:2
            
        MDLabel:
            text: 'hello world'
            halign: 'center'
            
        MDBottomAppBar:
            MDTopAppBar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: app.navigation_draw()
                mode: 'center'
"""
# BoxLayout = setiap kali kita ingin menumpuk elemen kita secara vertikal / horizontal
#orientation: 'vertical' = menumpuk elemen secara vertikal, karna kita akan membuat toolbar
#untuk toolbarnya pake MDTopAppBar. title = judul toolbarnya 
#left_action_items = menambahkan item(bisa berisi ikon) disebelah kiri dan memasukkan fungsi aksinya
#itu bertipe list, jadikita bisa memasukkan banyak item. ["menu", lambda x: app.navigation_draw()] == "menu" = ikon menu
#lambda x: app.navigation_draw() = ini untuk aksi saat user menekan item/ikonnya, fungsinya di navigation_draw()
#right_action_items = sama aja kaya left_action_items, ini bedanya itemnya ada disebelah kanan
#fungsi lambda x: yang di left_action_items&right_action_items = ini emang disuruh pake awalnya fungsi lamda
#elevation = ini untuk bayangannya topbar ini. jadi topbarnya ada efek kaya mengambang
## toolbar bawah
#pake MDBottomAppBar, lalu didalamnya pake MDTopAppBar
#icon = untuk iconnya, ini berbentuk bulat. on_action_button = untuk aksi icon yang berbentuk bulat tadi
#langsung masukkin fungsi yang berisi aksinya tanpa menggunakan lambda.
#mode = untuk posisi icon tombol yang berbentuk bulat: ’free-end’,’free-center’,’end’,’center’


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Red" # tema itemnya merah
        screen = Builder.load_string(screen_helper)
        return screen
    ## fungsi untuk aksi saat user mengklik icon menu ditopbarnya
    def navigation_draw(self):
        print("Navigation")

DemoApp().run()