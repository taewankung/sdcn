'''
Created on Jan 14, 2015

@author: aran
'''
from kivy.lang import Builder
import os

Builder.load_file(os.path.dirname(__file__) + '/music.kv')

from .submenu import SubMenu
class MusicMenu(SubMenu):
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)