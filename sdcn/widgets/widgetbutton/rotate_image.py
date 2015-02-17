'''
Created on Feb 9, 2015

@author: aran
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
from sdcn.widgets.widgetbutton.workflowwidget import WorkflowWidget
Builder.load_file(os.path.dirname(__file__) + '/rotate_image.kv')
class RotateImage(WorkflowWidget):
    def __init__(self,workflow_layout):
        super().__init__(workflow_layout)

class TestApp(App):
    def build(self):
        return RotateImage()
       
if __name__ == '__main__':
    TestApp().run()