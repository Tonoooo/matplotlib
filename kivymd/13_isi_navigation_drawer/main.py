# sumber :  https://youtu.be/WofR48auycs
## ini merupakan lanjutan dari 12_navigation_drawer

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (300, 500) # kita menetapkan ukuran window, ini hanya untuk mempermudah membuat apknya

## aliran proses
# MDScreen -> MDNavigationLayout -> MDScreenManager -> MDNavigationDrawer -> MDNavigationDrawerMenu -> isi
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
                    
            MDScreen:
                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: "images.jpg"
        
        MDNavigationDrawer:
            id: nav_drawer
            
            MDNavigationDrawerMenu:
                MDNavigationDrawerHeader:
                    title: "Judul Header"
                    text: "Text header"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "36dp"
                    
                MDNavigationDrawerItem
                    icon:  "face-man-profile"
                    text: "Profile"
                    
                MDNavigationDrawerItem
                    icon: "file-upload"
                    right_text: "+99"
                    text: "file-upload"
                    
                MDNavigationDrawerDivider
                    
                MDNavigationDrawerLabel:
                    text: "Keluar"
                    font_style: "Subtitle1"
                    
                MDNavigationDrawerItem
                    icon: "logout"
                    text: "Logout"
"""
## penjelasan
# untuk logo/gambar dinavigasinya belum bisa, dimasukin gambarnya jadi gede
# padding: "12dp", 0, 0, "36dp" --> padding: kiri, atas, kanan, bawah. dp atau piksel
# MDNavigationDrawerDivider untuk membuat gari horizontal

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


DemoApp().run()