from kivy.app import App
from kivy.uix.label import Label

class RootAssistantApp(App):
    def build(self):
        return Label(text="Selam Enes, AI Root burada!", font_size='20sp')

if __name__ == '__main__':
    RootAssistantApp().run()
