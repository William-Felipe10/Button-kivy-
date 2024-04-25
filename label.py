
from kivy.app import App 
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout

class MinhaApp(App):

    def build(self):
        return Label(text='Olá, SENAI',
            halign='center',   # Alinha o texto à esquerda
            valign ='buton',
            size_hint = (None, None),
            size = (200, 200),
            text_size = (None, None),
            font_size = 100,
            font_name='Arial',
            color= get_color_from_hex('#FF5733')
            
            )
 
    
if __name__ == "__main__":
    MinhaApp().run()



