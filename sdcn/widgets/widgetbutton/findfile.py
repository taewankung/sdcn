'''
Created on Jan 26, 2015

@author: aran
'''
from sdcn.widgets.widgetbutton.workflowwidget import WorkflowWidget
# from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
from .my_filechooser import MyFilechooser
Builder.load_file(os.path.dirname(__file__) + '/findfile.kv')
class FindFile(WorkflowWidget):
    filechooser_in_pop = MyFilechooser(title = 'Find file')
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)
    popup_filechoser = MyFilechooser(title = 'Find file')
    popup_filechoser.filechooser.multiselect = True

    def open_file_chooser(self):
        self.popup_filechoser.open()
        self.filechooser_in_pop = self.popup_filechoser
        self.path = self.filechooser_in_pop.filechooser.path
        self.popup_filechoser.filechooser.path = self.ids.path_input.text
        #         print(self.path)

class TestApp(App):
     def build(self):
         return FindFile()
 
if __name__ == '__main__':
     TestApp().run()
     
