'''
Created on Jan 14, 2015

@author: taewankung
'''
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import os

Builder.load_file(os.path.dirname(__file__) + '/controller.kv')
class SdcnController(BoxLayout):
    pass