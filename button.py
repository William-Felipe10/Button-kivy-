from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

def botao_pressionado(instance):
    print('Botão pressionado!')

class MinhaApp(App):
    def build(self):
        btn = Button(text='Clique aqui')
        btn.bind(on_press=botao_pressionado)
        return btn
'''
class MinhaApp(App):
    def build(self):
        return Button(text='Se clicar é viado', font_size = 50, background_color = get_color_from_hex('#3498db'))
'''

if __name__ == '__main__':
    MinhaApp().run()