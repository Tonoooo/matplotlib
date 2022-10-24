screen_helper = """
ScreenManager:
    LayarMenu:
    LayarProfil:
    LayarUpload:
    
<LayarMenu>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: 
            root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: 
            root.manager.current = 'upload'
    
<LayarProfil>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "left"
        
<LayarUpload>:
    name: 'upload'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'menu'
            root.manager.transition.direction = "left"
        
"""
## penjelasan
# mengatur layar/halaman yang akan ada didalam layar. ini kumpulan layar layarnya
# ScreenManager:
    # LayarMenu:
    # LayarProfil:
    # LayarUpload:
    #jika ada halaman lagi, masukkan disini. tapi buat dulu class nya difile py

# name: 'menu' # nama ini akan menjadi sebutan/panggilan diantara layar
# Untuk menambahkan navigasi di antara halaman kita, kita hanya perlu menambahkan acara on_press ke setiap tombol kita.

# <LayarMenu>, <LayarProfil>, <LayarUpload> inti nya yang ada <> kita harus 
#membuat class di python nya