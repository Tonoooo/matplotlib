# sumber : https://github.com/attreyabhatt/KivyMD-Basics/tree/master/8%20-%20List
from kivymd.app import MDApp
from kivy.lang import Builder

list_helper = """
MDScreen:
    ScrollView:
        MDList:
            OneLineListItem:
                text: 'Item1'
            OneLineListItem:
                text: 'Item2'
            ThreeLineListItem
                text: 'judul'
                secondary_text: 'qwerty'
                tertiary_text: 'zxcvbnm'
"""


class DemoApp(MDApp):

    def build(self):
        list = Builder.load_string(list_helper)
        return list


DemoApp().run()