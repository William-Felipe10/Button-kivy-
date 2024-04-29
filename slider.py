from kivy.app import App
from kivy.uix.slider import Slider

class Testando(App):
    def build(self):
        return Slider(min=0, max=1000, value=400)
    
if __name__ == "__main__":
    Testando().run()