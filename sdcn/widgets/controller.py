'''
Created on Jan 14, 2015

@author: taewankung
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from .pdfMenu import PdfMenu
from .document_menu import DocumentMenu
from .fileandfoldermenu import FileAndFolder
from .picturemenu import PictureMenu
from .videomenu import VideoMenu
from .musicmenu import MusicMenu
import os
from kivy.uix.button import Button
from .operation import Finder
Builder.load_file(os.path.dirname(__file__) + '/controller.kv')

class Layout_box3(BoxLayout):
    count = 0
    pass
class SdcnController(BoxLayout):
    #pdf_layout = BoxLayout()
    pdfs = PdfMenu()
    document = DocumentMenu()
    files = FileAndFolder()
    pic = PictureMenu()
    music = MusicMenu()
    video = VideoMenu()
    layouts = Layout_box3()
    layouts.add_widget(document.layout)
    #pdf_layout.add_widget(pdfs)
    def do_action_document(self):
        print("ss" + str(self.document.finder_num))
        self.box_wid2.add_widget(self.document)
        self.document_button.disabled = True
        if (self.file_button.disabled == True):
            self.box_wid2.remove_widget(self.files)
        elif (self.pic_button.disabled == True):
            self.box_wid2.remove_widget(self.pic)
        elif (self.pdf_button.disabled == True):
            self.box_wid2.remove_widget(self.pdfs)
        elif (self.video_button.disabled == True):
            self.box_wid2.remove_widget(self.video)
        elif (self.music_button.disabled == True):
            self.box_wid2.remove_widget(self.music)
        self.file_button.disabled = False
        self.pdf_button.disabled = False
        self.pic_button.disabled = False
        self.music_button.disabled = False
        self.video_button.disabled = False        
        if(self.layouts.count == 0):
            self.box_wid3.add_widget(self.layouts)
            self.layouts.count = 1
    
#     document.test
        
    def do_action_files(self):
        self.box_wid2.add_widget(self.files)
        if (self.document_button.disabled == True):
            self.box_wid2.remove_widget(self.document)
        elif (self.pic_button.disabled == True):
            self.box_wid2.remove_widget(self.pic)
        elif (self.pdf_button.disabled == True):
            self.box_wid2.remove_widget(self.pdfs)
        elif (self.video_button.disabled == True):
            self.box_wid2.remove_widget(self.video)
        elif (self.music_button.disabled == True):
            self.box_wid2.remove_widget(self.music)
        self.file_button.disabled = True
        self.pdf_button.disabled = False
        self.pic_button.disabled = False
        self.document_button.disabled = False
        self.music_button.disabled = False
        self.video_button.disabled = False
        self.box_wid3.remove_widget(self.document.layout)
        
    def do_action_pic(self):
        self.box_wid2.add_widget(self.pic)
        if (self.file_button.disabled == True):
            self.box_wid2.remove_widget(self.files)
        elif (self.document_button.disabled == True):
            self.box_wid2.remove_widget(self.document)
        elif (self.pdf_button.disabled == True):
            self.box_wid2.remove_widget(self.pdfs)
        elif (self.video_button.disabled == True):
            self.box_wid2.remove_widget(self.video)
        elif (self.music_button.disabled == True):
            self.box_wid2.remove_widget(self.music)
        self.pic_button.disabled = True
        self.file_button.disabled = False
        self.document_button.disabled = False
        self.pdf_button.disabled = False
        self.music_button.disabled = False
        self.video_button.disabled = False
        self.box_wid3.remove_widget(self.document.layout)
        
    def do_action_pdf(self):
        self.box_wid2.add_widget(self.pdfs)
        if (self.file_button.disabled == True):
            self.box_wid2.remove_widget(self.files)
        elif (self.pic_button.disabled == True):
            self.box_wid2.remove_widget(self.pic)
        elif (self.document_button.disabled == True):
            self.box_wid2.remove_widget(self.document)
        elif (self.video_button.disabled == True):
            self.box_wid2.remove_widget(self.video)
        elif (self.music_button.disabled == True):
            self.box_wid2.remove_widget(self.music)
        self.pdf_button.disabled = True
        self.file_button.disabled = False
        self.document_button.disabled = False
        self.pic_button.disabled = False
        self.music_button.disabled = False
        self.video_button.disabled = False
        self.box_wid3.remove_widget(self.document.layout)
        
    def do_action_video(self):
        self.box_wid2.add_widget(self.video)
        if (self.document_button.disabled == True):
            self.box_wid2.remove_widget(self.document)
        elif (self.file_button.disabled == True ):
            self.box_wid2.remove_widget(self.files)
        elif (self.pic_button.disabled == True ):
            self.box_wid2.remove_widget(self.pic)
        elif (self.pdf_button.disabled == True):
            self.box_wid2.remove_widget(self.pdfs)
        elif (self.music_button.disabled == True):
            self.box_wid2.remove_widget(self.music)
        self.video_button.disabled = True
        self.document_button.disabled = False
        self.file_button.disabled = False
        self.pic_button.disabled = False
        self.pdf_button.disabled = False
        self.music_button.disabled = False
        self.box_wid3.remove_widget(self.document.layout)
        
    def do_action_music(self):
        self.box_wid2.add_widget(self.music)
        if (self.document_button.disabled == True):
            self.box_wid2.remove_widget(self.document)
        elif (self.file_button.disabled == True ):
            self.box_wid2.remove_widget(self.files)
        elif (self.pic_button.disabled == True ):
            self.box_wid2.remove_widget(self.pic)
        elif (self.pdf_button.disabled == True):
            self.box_wid2.remove_widget(self.pdfs)
        elif (self.video_button.disabled == True):
            self.box_wid2.remove_widget(self.video)
        self.music_button.disabled = True
        self.document_button.disabled = False
        self.file_button.disabled = False
        self.pic_button.disabled = False
        self.pdf_button.disabled = False
        self.video_button.disabled = False
        self.box_wid3.remove_widget(self.document.layout)
    
    