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

Builder.load_file(os.path.dirname(__file__) + '/controller.kv')
class SdcnController(BoxLayout):
    #pdf_layout = BoxLayout()
    pdfs = PdfMenu()
    document = DocumentMenu()
    files = FileAndFolder()
    pic = PictureMenu()
    music = MusicMenu()
    video = VideoMenu()
    
    #pdf_layout.add_widget(pdfs)
    def do_action_document(self):
        self.box_wid2.add_widget(self.document)
        if(self.document.num == 0):
            self.box_wid3.add_widget(self.document.layout)
        if(self.document.num > 0):
            self.box_wid3.remove_widget(self.document.layout)
            self.box_wid3.add_widget(self.document.layout)
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