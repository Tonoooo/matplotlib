from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    padding: "10dp"
    MDBoxLayout:
        orientation:'horizontal'
        spacing: 10 # jarak antar elemen
        padding: 10
        MDCard:
            radius: 36 # seberapa melengkungnya pojok sisinya
            md_bg_color: "grey"
            pos_hint: {"center_x": .5, "center_y": .7}
            size_hint: .2, .4 # ukuran cardnya
            
            FitImage:
                source: "images.jpg"
                size_hint_y: .35
                pos_hint: {"top": 1}
                
        MDCard:
            radius: 36
            size_hint: .2, .4
            pos_hint: {"center_x": .5, "center_y": .7}
            focus_behavior: True # saat kursor / sentuhan diarahkan ke card ini maka dsini kita bisa ubah warnanya
            md_bg_color: "darkgrey" # warna backgroundnya
            focus_color: "grey" # warna saat kursor/sentuhan berada dicard ini
            unfocus_color: "darkgrey" # warna saat kursor/sentuhan tidak dicard ini
            elevation: 2
            on_release: app.aa() # saat card ini diklik maka fungsi aa yang dipython berjalan
            MDLabel:
                text: "bisa diklik"
                halign: "center"
            
    MDBoxLayout:
        orientation:'horizontal'
        spacing: 10
        padding: 10
        MDCard:
            radius: 36
            size_hint: .2, .4
            pos_hint: {"center_x": .5, "center_y": .2}
            md_bg_color: "darkgrey"
            elevation: 2
            on_release: app.aa()
            MDLabel:
                text: "bisa diklik"
                halign: "center"
            
        MDCard:
            radius: 36
            size_hint: .2, .4
            focus_behavior: True
            pos_hint: {"center_x": .5, "center_y": .2}
            md_bg_color: "darkgrey"
            unfocus_color: "darkgrey"
            focus_color: "grey"
            elevation: 2
            on_release: app.aa()
            MDIconButton:
                icon: "dots-vertical"
                pos_hint: {"top": 1, "left": 1}

'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)
    def aa(self):
        print("sdf")


Example().run()