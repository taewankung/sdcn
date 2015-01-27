'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
Builder.load_file(os.path.dirname(__file__) + '/resize_picture.kv')
class ResizePicture(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return ResizePicture()
       
if __name__ == '__main__':
    TestApp().run()