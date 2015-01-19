from kivy.lang import Builder
import os
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
Builder.load_file(os.path.dirname(__file__) + '/operation_doc.kv')
class Finder(StackLayout):
    num = 0
    def del_finder(self):
        print(self.num)
        self.num=1
        print(self.num)
        
    pass
class Doc_to_text(StackLayout):
    pass
class Doc_to_html(StackLayout):
    pass
class Compress_file(StackLayout):
    pass
class Hinden_file(StackLayout):
    pass
