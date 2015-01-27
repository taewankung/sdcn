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
Builder.load_file(os.path.dirname(__file__) + '/convert_file.kv')
class ConvertFile(StackLayout):
    pass
class TestApp(App):
    def build(self):
        return ConvertFile()
       
if __name__ == '__main__':
    TestApp().run()
           