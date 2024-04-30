from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video(source = 'C:/Users/aluno.sesipaulista\Downloads/20770858-hd_1080_1920_30fps.mp4')
    
if __name__ == "__main__":
    MinhaApp().run()