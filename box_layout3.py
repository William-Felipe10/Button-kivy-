from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label

class Mykkk(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical', spacing = 10)

        # CRIANDOE ADICIONANDO UM BOTÃO COM TEXTO, COR DE FUNDO E TAMANHO DE FONTE PERSONALIZADOS
        botao1 = Button(text = 'Botão 1', background_color = (0.2,0.7,0.3, 1), font_size = 20)
        layout.add_widget(botao1)

        # CRIANDO E ADICIONANDO UM BOTÃO COM UM TEXTO DIFERENTE E ALINHAMENTO HORIZONTAL PERSONALIZADO
        botao2 = Button(text = 'Clique Aqui!', halign = 'center')
        layout.add_widget(botao2)

        # CRIANDO E ADICIONANDO UM BOTÃO COM UM TEXTO GRANDE E COR DE FUNDO PERSONALIZADA
        botao3 = Button(text = 'Clique para continuar', background_color = (0.9,0.5,0.1,1), font_size = 30)
        layout.add_widget(botao3)

        # CRIANDO E ADICIONANDO UM BOTÃO COM UMA AÇÃO PERSONALIZADA AO SER PRESSIONADO
        def acao_botao(instance):
            instance.text = 'Botão Pressionado!'
        botao4 = Button(text = 'Botão 4')
        botao4.bind(on_press = acao_botao)
        layout.add_widget(botao4)

        # ADICIONANDO U RÓTULO PARA EXIBIR INFORMAÇÕES ADICIONAIS
        info_label = Label(text = 'Pressione os canhoes para ver diferentes propriedades em ação.')
        layout.add_widget(info_label)

        return layout
    
if __name__ == "__main__":
    Mykkk().run()