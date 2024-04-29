from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout_principal = BoxLayout(orientation = 'vertical')

        # WIDGET DE ENTRADA PARA O NOME DO USUÁRIO
        self.input_nome = TextInput(hint_text = 'Digite seu nome')
        layout_principal.add_widget(self.input_nome)

        # BOTÃO PARA ENVIAR O NOME E EXIBIR A MENSAGEM
        botao_enviar = Button(text = 'Enviar', on_press = self.exibir_mensagem)
        layout_principal.add_widget(botao_enviar)

        # LABEL PARA EXIBIR A MENSAGEM
        self.label_mensagem = Label()
        layout_principal.add_widget(self.label_mensagem)

        return layout_principal
    
    def exibir_mensagem(self, instance):
        nome_usuario = self.input_nome.text
        mensagem = f'Olá {nome_usuario}! Você está avançando no Kivy!'

if __name__ == "__main__":
    MyApp().run()