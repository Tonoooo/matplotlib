# sumber :  https://youtu.be/tcnKm1kcep8
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500) # kita menetapkan ukuran window, ini hanya untuk mempermudah membuat apknya

## aliran topbarnya
# MDScreen -> MDNavigationLayout -> MDScreenManager -> MDScreen -> MDTopAppBar
## aliran untuk isi navigasinya(sidebar)
# MDScreen -> MDNavigationLayout -> MDNavigationDrawer -> isi navigasinya
navigation_helper = """
MDScreen:
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDTopAppBar:
                    title: "Navigation Drawer"
                    elevation: 2
                    left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                    pos_hint: {"top": 1}
        MDNavigationDrawer:
            id: nav_drawer
"""
# pos_hint: {"top": 1} = agar si toolbarnya ada diatas
# lambda x: nav_drawer.set_state("open") = saat icon menu yang ditopbarnya dipencet
#maka MDNavigationDrawer akan dipanggil (menampilkan sidebarnya), penjelasannya saat iconnya dipencet maka si fungsi
#lambdanya akan merujuk ke nav_drawer, nah sinav_drawer ini adalah id dari MDNavigationDrawer lalu set_state("open")
#maksudnya saat dipencet icon menunya si navigasinya(sidebar) akan terbuka

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()