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
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
class SubMenu(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        
        self.bh = int(.075*self.workflow_layout.height)
        
        
    def add_to_workflow_layout(self, button):
        new_label = Label(text=button.text, size_hint_x=1,
                            size_hint_y=0.5,)
        layout = StackLayout(size_hint = (1,None),size = (self.workflow_layout.width,self.bh*2))
        layout.add_widget(new_label)
        if new_label.text == 'Find File':
            filechoser_layout = StackLayout( orientation="lr-bt")
            filechoser = FileChooserListView( size_hint = (0.75,1), size=(1,400))
            filechoser_layout.add_widget(filechoser)
            ok_button = Button(text = 'Ok' , size_hint = (0.12,None), size=(1,25))
            exit_button = Button(text = 'Exit' ,size_hint = (0.12,None), size=(1,25))
            filechoser_layout.add_widget(ok_button)
            filechoser_layout.add_widget(exit_button)
            browser_button = Button(text = 'Browser', size_hint = (1,None),size = (1, self.bh))
            popup_browser = Popup(title = 'Find file')
            popup_browser.add_widget(filechoser_layout)
            exit_button.bind(on_press = popup_browser.dismiss)
            browser_button.bind(on_press = popup_browser.open)
            layout.add_widget(browser_button)
            
        elif new_label.text == 'Resize Photo':
            
            text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,25))
            l = Label(text='Example: ....', font_size='15sp', size_hint_y=None)
            l.bind(width=lambda s, w:
                   s.setter('text_size')(s, (w, None)))
            l.bind(texture_size=l.setter('size'))
            layout.add_widget(text_input)
            layout.add_widget(l)
           
            
        self.workflow_layout.add_widget(layout)
        