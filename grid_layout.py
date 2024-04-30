from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Seila(App):
    def build(self):
        layout = GridLayout(cols = 2, spacing = [10,10], padding = [20,20])
        for i in range(4):
            botao = Button(text = f'Botão {i+1}')
            layout.add_widget(botao)

        return layout
    
if __name__ == "__main__":
    Seila().run()