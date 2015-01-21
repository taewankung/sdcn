'''
Created on Dec 26, 2014

@author: returner
'''


#standard ตัวเก็บพวกเมนูอะไรประมาณนี้
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

from .widgets.controller import SdcnController

class SdcnApplication(App):
    def build(self):
        return SdcnController()