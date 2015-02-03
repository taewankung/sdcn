'''
Created on Jan 28, 2015

@author: taewankung
'''
from kivy.uix.popup import Popup
from kivy.app import App
from kivy.lang import Builder
import os
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
Builder.load_file(os.path.dirname(__file__) + '/my_filechooser.kv')
class MyFilechooser(Popup):
    path = '/'
    def okfile(self):
        print(self.filechooser.path)
        self.path = self.filechooser.path
        self.selection = self.filechooser.selection
        self.dismiss()
        
    def cancels(self):
        self.dismiss()#                     print(selection_file)
    pass

class TestApp(App):
    def build(self):
        s = StackLayout()
        p = MyFilechooser(title = 'test')
        b = Button(size_hint = (1,0.2))
        b.bind(on_press = p.open)
        s.add_widget(b)
        return s
    
if __name__ == '__main__':
     TestApp().run()