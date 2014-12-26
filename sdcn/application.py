'''
Created on Dec 26, 2014

@author: returner
'''


from kivy.app import App
from kivy.uix.button import Button

class SdcnApplication(App):
    def build(self):
        return Button(text='Hello World')