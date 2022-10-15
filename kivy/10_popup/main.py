# sumber : https://youtu.be/PpLuyOzCKTQ

from kivy.app import App
from kivy.uix.widget import Widget # kita gunakan untuk tampilan app
from kivy.uix.floatlayout import FloatLayout # kita gunakan untuk tampilan popup
from kivy.uix.popup import Popup # ini popup nya


class Widgets(Widget):
    # membuat aksi untuk tombol di app nya
    def btn(self): # ketika tombol di appnya ditekan popup nya akan muncul
        show_popup() # memanggil fungsi popup nya

# membuat kelas baru yang akan menyimpan konten popup kita. Saya akan memanggil milik saya "P". 
#Ini akan mewarisi dari FloatLayout sehingga saya dapat menggunakan size_hint dan pos_hint.
class P(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return Widgets()

# membuat fungsi di suatu tempat dalam program kita yang akan bertanggung jawab untuk menampilkan popup.
#Sekarang setiap kali kita memanggil fungsi show_popup() popup akan ditampilkan.
def show_popup():
    # membuat objek baru dari kelas P(), class P mengandung bentuk tampilan popupnya
    show = P() 
    # buat popup nya
    popupWindow = Popup(title="Ini Judul Popup", content=show, size_hint=(None,None),size=(250,250))
    #size_hint=(None,None) karna kita tidak ingin mengubah ukuran secara dinamis. size=(400,400) = ukuran popupnya
    popupWindow.open() # tampilkan popup


if __name__ == "__main__":
    MyApp().run()