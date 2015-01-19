'''
Created on Jan 14, 2015

@author: aran
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from .operation import Finder
import os
from kivy.uix.button import Button
from .operation import auto


Builder.load_file(os.path.dirname(__file__) + '/docmenu.kv')
class DocumentMenu(StackLayout):
    finder_num = 0
#     layout = StackLayout(size_hint = (1,0.075))
#     order_box = Order()
#     num = 0
    def call_button(self):
        print(self.finder_num)
        self.finder_num += 1
        print(self.finder_num)
        #auto(self)
#         if(self.document.finder_num == 0):
#             self.box3_layout.add_widget(Finder())
#         if(self.document.finder_num > 0):
#             self.box3_layout.remove_widget(Finder())
#             self.box3_layout.add_widget(Finder())
#         self.num += 1
#         self.order_box.layout.add_widget(self.order_box.Finder())
#         print(self.num)
#         if(self.num == 0):
#             self.layout.add_widget(self.order_box.layout)
#         if(self.num > 0):
#             self.layout.remove_widget(self.order_box.layout)
#             self.layout.add_widget(self.order_box.layout)        
#         for i in range(self.num):
#             btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
#             self.layout.add_widget(btn)
    pass