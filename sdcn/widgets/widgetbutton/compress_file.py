'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
from sdcn.widgets.widgetbutton.deleteable import WorkflowWidget
Builder.load_file(os.path.dirname(__file__) + '/compress_file.kv')
class CompressFile(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return CompressFile()
       
if __name__ == '__main__':
    TestApp().run()
           