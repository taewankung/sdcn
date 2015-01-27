'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
Builder.load_file(os.path.dirname(__file__) + '/rename_image.kv')
class RenameImage(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return RenameImage()
       
if __name__ == '__main__':
    TestApp().run()