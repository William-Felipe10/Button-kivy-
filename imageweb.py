from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source="https://th.bing.com/th/id/OIP.j0YD7es22_kyBypqdLENaQHaE8?rs=1&pid=ImgDetMain")
    
if __name__ == '__main__':
    MinhaApp().run()