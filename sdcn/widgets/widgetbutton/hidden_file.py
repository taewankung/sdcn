'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
Builder.load_file(os.path.dirname(__file__) + '/hidden_file.kv')
class HiddenFile(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return HiddenFile()
       
if __name__ == '__main__':
    TestApp().run()