'''
Created on Jan 21, 2015

@author: boatkrap
'''

from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.uix.spinner import Spinner
from sdcn.widgets.widgetbutton.convert_pdf_file import  ConvertPDFFile
from sdcn.widgets.widgetbutton.findfile import FindFile 
from sdcn.widgets.widgetbutton.add_photo_to_album import AddPhotoToAlbum
from sdcn.widgets.widgetbutton.convert_file import ConvertFile
from sdcn.widgets.widgetbutton.compress_file import CompressFile
from sdcn.widgets.widgetbutton.hidden_file import HiddenFile
from sdcn.widgets.widgetbutton.new_folder import NewFolder
from sdcn.widgets.widgetbutton.resize_image import ResizeImage
from sdcn.widgets.widgetbutton.crop_image import CropImage
from sdcn.widgets.widgetbutton.rename_image import RenameImage
from sdcn.widgets.widgetbutton.change_image_type import ChangeImageType
from sdcn.widgets.widgetbutton.convert_music_type import ConvertMusicType
from sdcn.widgets.widgetbutton.convert_video import ConvertVideoType
from sdcn.widgets.widgetbutton.resize_video import ResizeVideo
from sdcn.widgets.widgetbutton.workflowwidget import DraggableWidgetContainer

from sdcn.garden.magnet import Magnet
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import os
from sdcn.widgets.widgetbutton.rotate_image import RotateImage

class DraggableSubmenuContainer(Magnet):
    menu = ObjectProperty(None, allownone=True)
    app = ObjectProperty(None)

    def on_menu(self, *args):
        self.clear_widgets()

        if self.menu:
            Clock.schedule_once(lambda *x: self.add_widget(self.menu), 0)

    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.remove_widget(self.menu)
            self.center = touch.pos
            self.menu.center = touch.pos
            self.app.root.add_widget(self.menu)
            return True

        return super().on_touch_down(touch, *args)

    def on_touch_move(self, touch, *args):
        grid_layout = self.app.root.ids.grid_layout
        float_layout = self.app.root.ids.float_layout

        if touch.grab_current == self:
            self.img.center = touch.pos
            if grid_layout.collide_point(*touch.pos):
                grid_layout.remove_widget(self)
                float_layout.remove_widget(self)

                for i, c in enumerate(grid_layout.children):
                    if c.collide_point(*touch.pos):
                        grid_layout.add_widget(self, i - 1)
                        break
                else:
                    grid_layout.add_widget(self)
            else:
                if self.parent == grid_layout:
                    grid_layout.remove_widget(self)
                    float_layout.add_widget(self)

                self.center = touch.pos

        return super().on_touch_move(touch, *args)

    def on_touch_up(self, touch, *args):
        if touch.grab_current == self:
            self.app.root.remove_widget(self.menu)
            self.add_widget(self.menu)
            touch.ungrab(self)
            return True

        return super().on_touch_up(touch, *args)


        
class SubMenu(StackLayout):
    menu_path = os.path.dirname(__file__)
    
    def __init__(self, workflow_layout, main_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.main_layout = main_layout
        self.bh = int(.075*self.workflow_layout.height)
        
        
        
    def add_to_workflow_layout(self, button):
        self.add_widget_to_workflow_layout(button.text)
        
    def add_widget_to_workflow_layout(self, text):

        dw = None
        if text == 'Find File':
            dw = DraggableWidgetContainer(widget=FindFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,150))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Compress Files':
            dw = DraggableWidgetContainer(widget=CompressFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,150))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
            
        elif text == 'Convert Files':
            dw = DraggableWidgetContainer(widget=ConvertFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Hidden Files':
            dw = DraggableWidgetContainer(widget=HiddenFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)

        elif text == 'New Folder':
            dw = DraggableWidgetContainer(widget=NewFolder(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Add Image To Album':
            dw = DraggableWidgetContainer(widget=AddPhotoToAlbum(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Resize Image':
            dw = DraggableWidgetContainer(widget=ResizeImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Crop Image':
            dw = DraggableWidgetContainer(widget=CropImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Rename Image':
            dw = DraggableWidgetContainer(widget=RenameImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Change Image Type':
            dw = DraggableWidgetContainer(widget=ChangeImageType(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Convert PDF File':
            dw = DraggableWidgetContainer(widget=ConvertPDFFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Convert Music Type':
            dw = DraggableWidgetContainer(widget=ConvertMusicType(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            dw.widget.ids.workflow_header.text = text
            self.workflow_layout.add_widget(dw)
        elif text == 'Resize Video':
            dw = DraggableWidgetContainer(widget=ResizeVideo(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        
        elif text == 'Rotate Image':
            dw = DraggableWidgetContainer(widget=RotateImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        
        elif text == 'Convert Video Type':
            dw = DraggableWidgetContainer(widget=ConvertVideoType(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        return dw
