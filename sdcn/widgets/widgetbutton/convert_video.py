'''
Created on Feb 9, 2015

@author: taewankung
'''
from kivy.lang import Builder
from sdcn.widgets.widgetbutton.workflowwidget import WorkflowWidget
import os
Builder.load_file(os.path.dirname(__file__) + '/convert_video.kv')

class ConvertVideoType(WorkflowWidget):
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)