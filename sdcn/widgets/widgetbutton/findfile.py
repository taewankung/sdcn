'''
Created on Jan 26, 2015

@author: aran
'''
from sdcn.widgets.widgetbutton.workflowwidget import WorkflowWidget
from os.path import expanduser
# from kivy.uix.spinner import Spinner
from kivy.lang import Builder
import os
from kivy.app import App
from .my_filechooser import MyFilechooser
Builder.load_file(os.path.dirname(__file__) + '/findfile.kv')
class FindFile(WorkflowWidget):
    popup_filechoser = MyFilechooser(title = 'Find file')
    popup_filechoser.filechooser.multiselect = True
    first_path = expanduser('~')
    popup_filechoser.filechooser.path = first_path
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)
    def open_file_chooser(self):
        print(self.popup_filechoser.filechooser.path)
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
     
