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
from sdcn.widgets.widgetbutton.workflowwidget import DraggableWidgetContainer

from sdcn.garden.magnet import Magnet
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.clock import Clock

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
    
    def __init__(self, workflow_layout, main_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.main_layout = main_layout
        self.bh = int(.075*self.workflow_layout.height)   
        
    def add_to_workflow_layout(self, button):
        new_label = Label(text=button.text, size_hint_x=0.89,
                            size_hint_y= 0.5)
#         layout = StackLayout(size_hint = (1,None),size = (self.workflow_layout.width,self.bh*2))
#         layout.add_widget(Delete_button())
        if new_label.text == 'Find File':
            dw = DraggableWidgetContainer(widget=FindFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,150))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Compress Files':
            dw = DraggableWidgetContainer(widget=CompressFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
            
        elif new_label.text == 'Convert Files':
            dw = DraggableWidgetContainer(widget=ConvertFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Hidden Files':
            dw = DraggableWidgetContainer(widget=HiddenFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)

        elif new_label.text == 'New Folder':
            dw = DraggableWidgetContainer(widget=NewFolder(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
# #Picture Menu*****************************************************************************************************************************          PICTURE
# 
#         elif new_label.text == 'Resize Photo': 
#             text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,25))
#             l = Label(text='Example: ....', font_size='15sp', size_hint_y=None)
#             l.bind(width=lambda s, w:
#             s.setter('text_size')(s, (w, None)))
#             l.bind(texture_size=l.setter('size'))
#             layout.add_widget(text_input)
#             layout.add_widget(l)
#         
#         elif new_label.text == 'Rename File':
#             text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,self.bh))
#             l = Label(text='Example: ....', font_size='15sp', size_hint_y = None)
#             l.bind(width=lambda s, w:
#             s.setter('text_size')(s, (w, None)))
#             l.bind(texture_size=l.setter('size'))
#             layout.add_widget(text_input)
#             layout.add_widget(l)
#         
        elif new_label.text == 'Add Image To Album':
            dw = DraggableWidgetContainer(widget=AddPhotoToAlbum(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Resize Image':
            dw = DraggableWidgetContainer(widget=ResizeImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Crop Image':
            dw = DraggableWidgetContainer(widget=CropImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Rename Image':
            dw = DraggableWidgetContainer(widget=RenameImage(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
        elif new_label.text == 'Change Image Type':
            dw = DraggableWidgetContainer(widget=ChangeImageType(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
#             pass
#         elif new_label.text == 'Crop Image':
#             label_x = Label(text = 'X:',size_hint=(0.25,None), size = (100,self.bh))
#             text_input_x = TextInput(size_hint=(0.24,None), size = (100,self.bh))
#             label_y = Label(text = 'y:',size_hint=(0.25,None), size = (100,self.bh))
#             text_input_y= TextInput(size_hint=(0.24,None), size = (100,self.bh))
#             layout.add_widget(label_x)
#             layout.add_widget(text_input_x)
#             layout.add_widget(label_y)
#             layout.add_widget(text_input_y)
#         elif new_label.text == 'Change File Type':
#             change_file_type = Spinner(text='.jpg',values=('.png', '.gif','.tif'),size_hint=(1,None),size=(1,44))
#             layout.add_widget(change_file_type)
# #END PIC*******************************************************************************************************************************END PIC
#         
#         elif new_label.text == 'Write File': 
#             pass
#         elif new_label.text == 'Add File':
#             pass
#         
#END FILE*******************************************************************************************************************************END FILE
        elif new_label.text == 'Convert PDF file':
            dw = DraggableWidgetContainer(widget=ConvertPDFFile(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)


#END PDF********************************************************************************************************************************END PDF
#         elif new_label.text == 'Convert Music Files':
#             change_file_music_type = Spinner(text='.mp3 to .wav',values=('.mp3 to .wav','.wav to.mp3','.mp4 to .mp3','.ra to .mp3','.mp3 to .ra','.mp3 to .au'),size_hint=(1,None),size=(1,44))
#             layout.add_widget(change_file_music_type)
        elif new_label.text == 'Convert Music Type':
            dw = DraggableWidgetContainer(widget=ConvertMusicType(self.workflow_layout),
                                          workflow_layout=self.workflow_layout,
                                          main_layout=self.main_layout,
                                          size_hint=(1,None),
                                          size=(1,100))
            self.workflow_layout.add_widget(dw)
# 
# #END MUSIC******************************************************************************************************************************END MUSIC
#         elif new_label.text == 'Convert Video Files':
#             change_file_video_type = Spinner(text='.dat to .mp4',values=('.dat to .mp4','.mp4 to .dat'),size_hint=(1,None),size=(1,44))
#             layout.add_widget(change_file_video_type)
#         elif new_label.text == 'Resize Video':
#             label_x = Label(text = 'X:',size_hint=(0.25,None), size = (100,self.bh))
#             text_input_x = TextInput(size_hint=(0.24,None), size = (100,self.bh))
#             label_y = Label(text = 'y:',size_hint=(0.25,None), size = (100,self.bh))
#             text_input_y= TextInput(size_hint=(0.24,None), size = (100,self.bh))
#             layout.add_widget(label_x)
#             layout.add_widget(text_input_x)
#             layout.add_widget(label_y)
#             layout.add_widget(text_input_y)    
#END Video******************************************************************************************************************************END Video
#         self.workflow_layout.add_widget(layout)
