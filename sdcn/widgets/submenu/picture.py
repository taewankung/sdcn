'''
Created on Jan 14, 2015

@author: aran
'''

from kivy.lang import Builder
from .submenu import SubMenu
import os

Builder.load_file(os.path.dirname(__file__) + '/picture.kv')
class PictureMenu(SubMenu):
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)