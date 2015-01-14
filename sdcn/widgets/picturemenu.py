'''
Created on Jan 14, 2015

@author: aran
'''

from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
import os

Builder.load_file(os.path.dirname(__file__) + '/picturemenu.kv')
class PictureMenu(BoxLayout):
    pass