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
from sdcn.widgets.submenu.Image import ImageMenu
from sdcn.widgets.submenu.video import VideoMenu
from sdcn.widgets.submenu.music import MusicMenu
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
import os
from kivy.uix.popup import Popup

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
                         ImageMenu(self.workflow_layout), MusicMenu(self.workflow_layout), VideoMenu(self.workflow_layout)]
        
        self.workflow_layout.bind(minimum_height=self.workflow_layout.setter('height'))
    def status_play_button(self):
        self.play_button.enable += 1
        
    def on_touch_down(self, touch):
        super().on_touch_down(touch)
        
        if self.play_button.enable%2 == 1 :
            self.play_button.background_normal = 'play1.png'
            self.play_button.background_down = 'pausee.png'
        else:
            self.play_button.background_normal = 'pausee.png'
            self.play_button.background_down = 'play1.png'
            
    def change_submenu(self, menu_name, button):
        for bt in self.main_menu_layout.children:
            if bt is button:
                bt.disabled = True
            else:
                bt.disabled = False
            
        for submenu in self.submenus:
            if submenu.__class__.__name__ == menu_name:
                self.sub_menu_layout.clear_widgets()
                self.sub_menu_layout.add_widget(submenu)
                break

    def save_as(self):
        filechoser_layout = StackLayout( orientation="lr-bt")
        filechoser = FileChooserListView( size_hint = (0.75,1), size=(1,400))
        filechoser_layout.add_widget(filechoser)
        ok_button = Button(text = 'Ok' , size_hint = (0.12,None), size=(1,25))
        cancel_button = Button(text = 'Cancel' ,size_hint = (0.12,None), size=(1,25))
        filechoser_layout.add_widget(ok_button)
        filechoser_layout.add_widget(cancel_button)
        popup_browser = Popup(title = 'Save As...')
        popup_browser.add_widget(filechoser_layout)
        cancel_button.bind(on_press = popup_browser.dismiss)
        popup_browser.open()
        pass