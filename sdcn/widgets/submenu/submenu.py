'''
Created on Jan 21, 2015

@author: boatkrap
'''

from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
class SubMenu(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        
        self.bh = int(.075*self.workflow_layout.height)
        
        
    def add_to_workflow_layout(self, button):
        new_label = Label(text=button.text, size_hint_x=1,
                            size_hint_y=None, size=(self.workflow_layout.width, self.bh))
        layout = StackLayout(size_hint = (None,None),size = (self.workflow_layout.width,self.bh*2))
        layout.add_widget(new_label)
        if new_label.text == 'Find File':
            filechoser_layout = BoxLayout()
            filechoser = FileChooserListView()
            filechoser_layout.add_widget(filechoser)
            exit_button = Button(text = 'Exit')
            filechoser_layout.add_widget(exit_button)
            browser_button = Button(text = 'Browser', size_hint = (None,None),size = (self.workflow_layout.width, self.bh))
            popup_browser = Popup(title = 'Find file')
            popup_browser.add_widget(filechoser_layout)
            exit_button.bind(on_press = popup_browser.dismiss)
            browser_button.bind(on_press = popup_browser.open)
            layout.add_widget(browser_button)
        self.workflow_layout.add_widget(layout)
        