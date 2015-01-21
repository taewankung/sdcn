'''
Created on Jan 21, 2015

@author: boatkrap
'''

from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class SubMenu(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        
    def add_to_workflow_layout(self, button):
        new_button = Button(text=button.text, size_hint_x=1,
                            size_hint_y=0.075)
        self.workflow_layout.add_widget(new_button)