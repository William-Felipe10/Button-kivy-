from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        video = Video(source = 'c:Users/aluno.sesipaulista/Videos/20770858-hd_1080_1920_30fps.mp4')
        video.state = 'play'
        video.options = {'eos' : 'loop'}
        video.allow_stretch = True

        return Video
    
if __name__ == "__main__":
    MinhaApp().run()