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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.bubble import Bubble
from kivy.lang import Builder
Builder.load_string('''
<Delete_button>
    size_hint: (None, None)
    size: (160, 60)
    pos_hint: {'center_x': .5, 'y': .6}
    BubbleButton:
        text: 'Delete'
        background_color: (1,0,0,2)
        
''')


class Delete_button(Bubble):
    pass

class ClickRightOption(Label):
    layout = FloatLayout()
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        if touch.button == 'right':
            print('right')
            if not hasattr(self, 'bubb'):
                self.bubb = bubb = Delete_button()
                self.layout.add_widget(bubb)
                self.add_widget(self.layout)
            else:
                values = ('left_top', 'left_mid', 'left_bottom', 'top_left',
                          'top_mid', 'top_right', 'right_top', 'right_mid',
                          'right_bottom', 'bottom_left', 'bottom_mid', 'bottom_right')
                index = values.index(self.bubb.arrow_pos)
                self.bubb.arrow_pos = values[(index + 1) % len(values)]
    def on_touch_up(self, touch):
        print('up')
#         for submenu in self.layout:
#             if submenu.__class__.__name__ == 'delete':
#                 self.layout.remove_widgets(submenu)
    pass

class SubMenu(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.bh = int(.075*self.workflow_layout.height)
        
        
    def add_to_workflow_layout(self, button):
        new_label = ClickRightOption(text=button.text, size_hint_x=1,
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
        
        elif new_label.text == 'Rename File':
            text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,25))
            l = Label(text='Example: ....', font_size='15sp', size_hint_y = None)
            l.bind(width=lambda s, w:
                   s.setter('text_size')(s, (w, None)))
            l.bind(texture_size=l.setter('size'))
            layout.add_widget(text_input)
            layout.add_widget(l)
           
            
        self.workflow_layout.add_widget(layout)
        
