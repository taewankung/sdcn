'''
Created on Jan 14, 2015

@author: aran
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from .operation import Finder
from .operation import Doc_to_text
from .operation import Doc_to_html
from .operation import Compress_file
from .operation import Hinden_file
import os
from kivy.uix.button import Button
# from sdcn.widgets.submenu.operation import auto


Builder.load_file(os.path.dirname(__file__) + '/document.kv')

class DocumentMenu(StackLayout):
    finder_num = 0
    layout = StackLayout(orientation= 'tb-lr')
    lout = Button(text = 'out',size_hint = (1,0.075))
#     layout.add_widget(lout)
#     order_box = Order()
    num = 0
    def call_button_finder(self):
        btn = Finder()
#         btn.bind(on_press = self.out)
        #self.layout.remove_widget(self.lout)
        self.layout.add_widget(btn)
        #self.layout.add_widget(self.lout)
    def call_button_doc_text(self):
        #self.layout.remove_widget(self.lout)
        self.layout.add_widget(Doc_to_text())
        #self.layout.add_widget(self.lout)
    def call_button_doc_html(self):
        #self.layout.remove_widget(self.lout)
        self.layout.add_widget(Doc_to_html())
        #self.layout.add_widget(self.lout)
    def call_button_Compress(self):
        #self.layout.remove_widget(self.lout)
        self.layout.add_widget(Compress_file())
        #self.layout.add_widget(self.lout)
    def call_button_hind(self):
        #self.layout.remove_widget(self.lout)
        self.layout.add_widget(Hinden_file())
        #self.layout.add_widget(self.lout)
    
#     lout.bind(on_press = out())
    
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