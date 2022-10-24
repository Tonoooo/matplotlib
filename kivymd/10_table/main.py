# sumber : https://youtu.be/HMnAg_izNcY

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable # untuk tabel nya
from kivy.metrics import dp # desplay pixel, disini kita gunakan untuk ukuran kolomnya berapa piksel


class DemoApp(MDApp):

    def build(self):
        screen = MDScreen()
        ## membuat tabel
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6), # lebar 90%, tinggi 60%
                                 check=True, # tombol ceklis berada dikiri. Secara default ini false
                                 rows_num=10, # berapa banyak baris tabel kita
                                 column_data=[ # untuk kolomnya. ini bertipe list
                                     ("No.", dp(18)), # ("nama kolom", lebar ukuran piksel)
                                     ("Food", dp(20)),
                                     ("Calories", dp(20))
                                 ],
                                 row_data=[ # untuk barisnya. ini bertipe list
                                     ("1", "Burger", "300"), # ("kolom no", "kolom burger", "kolom kalori"). Ini isi baris ke 1
                                     ("2", "Oats", "200"),# Ini isi baris ke 2
                                     ("3", "Oats", "200"),# Ini isi baris ke 3
                                     ("4", "Oats", "200"),# Ini isi baris ke 4
                                     ("5", "Oats", "200"),# Ini isi baris ke 5, dan seterusnya
                                     ("6", "Oats", "200"),
                                     ("7", "Oats", "200"),
                                     ("8", "Oats", "200")

                                 ]
                                 )
        ## untuk membinding/aksi jika ada baris yang diklik
        data_table.bind(on_row_press=self.on_row_press) #aksinya ada difungsi on_row_press
        ## untuk membinding/aksi jika ada baris yang diceklis
        data_table.bind(on_check_press=self.on_check_press) #aksinya ada difungsi on_check_press
        screen.add_widget(data_table)
        return screen
    # fungsi untuk aksi jika ada baris yang ditekan/diklik
    def on_row_press(self, instance_table, instance_row): # punya 2 parameter: instance_table, instance_row
        print(instance_table, instance_row)
    # fungsi untuk aksi jika ada baris yang diceklis
    def on_check_press(self, instance_table, current_row): # punya 2 parameter: instance_table, current_row
        print(instance_table, current_row)
        # current_row = berisi baris nya diceklis, contoh kita ceklis baris kesatu maka nilainya ['1', 'Burger', '300']


DemoApp().run()