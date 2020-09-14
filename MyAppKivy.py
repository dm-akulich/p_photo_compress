from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
import random
import time
import os
from MyAppLogic import *


class MainLayout(FloatLayout):

    artistName = StringProperty()

    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.artistName = "Перетащите папку с файлами"

class MainApp(App):

    def build(self):
        self.title = "Компрессор"
        Window.bind(on_dropfile=self._on_file_drop)
        Window.size = (600,400)
        self.mainLayout = MainLayout()
        return self.mainLayout

    def _on_file_drop(self, window, file_path):
        self.mainLayout.artistName = 'Готово'
        # print(file_path.decode("utf-8"))
        crawler(file_path.decode("utf-8"))
        compressor(list_of_images)
        return self.mainLayout

if __name__ == '__main__':
    MainApp().run()