'''
Created on Jan 26, 2015

@author: aran
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout

class WorkflowWidget(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
    def delete_in_workflow_layout(self, menu):
        for l in self.workflow_layout.children: 
            l.remove_widget(menu)
