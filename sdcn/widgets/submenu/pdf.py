'''
Created on Jan 14, 2015

@author: taewankung
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
import os

Builder.load_file(os.path.dirname(__file__) + '/pdf.kv')
class PdfMenu(StackLayout):
    pass