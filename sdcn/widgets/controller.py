'''
Created on Jan 14, 2015

@author: taewankung
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from sdcn.widgets.submenu.pdf import PdfMenu
from sdcn.widgets.submenu.document import DocumentMenu
from sdcn.widgets.submenu.fileandfolder import FileAndFolderMenu
from sdcn.widgets.submenu.picture import PictureMenu
from sdcn.widgets.submenu.video import VideoMenu
from sdcn.widgets.submenu.music import MusicMenu
import os
from kivy.uix.button import Button
from sdcn.widgets.submenu.operation import Finder
Builder.load_file(os.path.dirname(__file__) + '/controller.kv')


class SdcnController(BoxLayout):
    def __init__(self):
        super().__init__()
#         self.pdf_menu = PdfMenu()
#         self.document_menu = DocumentMenu()
#         self.file_munu = FileAndFolderMenu()
#         self.picture_menu = PictureMenu()
#         self.music_menu = MusicMenu()
#         self.video_menu = VideoMenu()
        
        
        self.submenus = [PdfMenu(self.workflow_layout), DocumentMenu(self.workflow_layout), FileAndFolderMenu(self.workflow_layout),
                         PictureMenu(self.workflow_layout), MusicMenu(self.workflow_layout), VideoMenu(self.workflow_layout)]

        
        
    def change_submenu(self, menu_name, button):
        for bt in self.main_menu_layout.children:
            bt.disabled = False
            
        for submenu in self.submenus:
            if submenu.__class__.__name__ == menu_name:
                button.disabled = True
                self.sub_menu_layout.clear_widgets()
                self.sub_menu_layout.add_widget(submenu)
                