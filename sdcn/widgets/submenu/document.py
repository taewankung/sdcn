'''
Created on Jan 14, 2015

@author: aran
'''
from kivy.lang import Builder
import os

from .submenu import SubMenu


Builder.load_file(os.path.dirname(__file__) + '/document.kv')

class DocumentMenu(SubMenu):
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)