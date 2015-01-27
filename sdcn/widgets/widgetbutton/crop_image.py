'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
Builder.load_file(os.path.dirname(__file__) + '/crop_image.kv')
class CropImage(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return CropImage()
       
if __name__ == '__main__':
    TestApp().run()