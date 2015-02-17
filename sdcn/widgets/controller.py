'''
Created on Jan 14, 2015

@author: taewankung
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
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

from sdcn import commands
from kivy.core.audio import SoundLoader 
from kivy.uix.label import Label
from sdcn.widgets.save_open.save_file import SavePopup
from sdcn.widgets.save_open.open_file import OpenPopup
import json
from io import StringIO
from sdcn.widgets.submenu.submenu import SubMenu


Builder.load_file(os.path.dirname(__file__) + '/controller.kv')


class SdcnController(FloatLayout):
    complete = Popup(title = 'Complete',size_hint=(0.5,0.5))
    complete.add_widget(Label(text = 'Complete'))
    
    def __init__(self):
        super().__init__()
#         self.pdf_menu = PdfMenu()
#         self.document_menu = DocumentMenu()
#         self.file_munu = FileAndFolderMenu()
#         self.picture_menu = PictureMenu()
#         self.music_menu = MusicMenu()
#         self.video_menu = VideoMenu()
        self.main_menu_layout = self.ids.main_menu_layout
        self.sub_menu_layout = self.ids.sub_menu_layout
        self.workflow_layout = self.ids.workflow_layout
        self.submenus = [PdfMenu(self.workflow_layout, self), DocumentMenu(self.workflow_layout, self), 
                         FileAndFolderMenu(self.workflow_layout, self), ImageMenu(self.workflow_layout, self), 
                         MusicMenu(self.workflow_layout, self), VideoMenu(self.workflow_layout, self)]
        self.workflow_layout.bind(minimum_height=self.workflow_layout.setter('height'))
   
    def status_play_button(self):
        self.ids.play_button.enable += 1
        if self.ids.play_button.enable % 2 == 0:
            self.ids.play_button.background_normal = '../sdcn/data/images/play1.png'
            self.ids.play_button.background_down = '../sdcn/data/images/pause1.png'
        elif self.ids.play_button.enable % 2 == 1 :
            self.ids.play_button.background_normal = '../sdcn/data/images/pause1.png'
            self.ids.play_button.background_down = '../sdcn/data/images/play1.png'
            command_output = None
            for bt in reversed(self.workflow_layout.children):
                print(bt.widget.__class__.__name__)
                if bt.widget.__class__.__name__ == 'FindFile':

                    path_file = str(bt.widget.popup_filechoser.filechooser.path)
                    selection_file = bt.widget.popup_filechoser.filechooser.selection
                    self.ids.out_label.text = path_file
#                     print(bt.widget.filechooser_in_pop.path)
#                     print(bt.widget.ids.file_input.text)
#                     test1 = ['find', str(path_file) ,  '-name',str(bt.widget.ids.file_input.text)]
#                     test = subprocess.check_output(test1)
#                     print(test)
#                     cmd = commands.FindCommand(path=path_file, pattern = str(selection_file[0]))
                    
                    cmd = commands.FindCommand(path=path_file, pattern = bt.widget.ids.file_input.text)
                    cmd_runner = commands.CommandRunner(cmd.build())
                    cmd_runner.start()
                    cmd_runner.join()
                    command_output = cmd_runner.output
                    if bt.widget.ids.file_input.text == '':
                        command_output = selection_file
                    print("output:", command_output)
                    
                elif bt.widget.__class__.__name__ == 'ConvertFile':
                    print(bt.widget.ids.type.text)
                    if bt.widget.ids.type.text == '.doc to Text':
#                         subprocess.call(['libreoffice', '--invisible', '--convert-to', 'txt:text', 'file1.docx']) 
#                     elif bt.widget.ids.type.text == '.doc to Html':
#                         print('doc to html')
                        if type(command_output) is list:
                            for i in command_output:
                                cmd = commands.ConvertFileCommand(source = i, target=i[:i.rfind('.')]+".pdf")
                                cmd_runner = commands.CommandRunner(cmd.build())
                                cmd_runner.start()
                                cmd_runner.join()
                                print(cmd_runner.output)
                                command_output = cmd_runner.output
                            
                elif bt.widget.__class__.__name__ == 'CompressFile':
                    print(bt.widget.ids.type.text)
                    if bt.widget.ids.type.text == '.Zip':
                        if(bt.widget.ids.name.text == ''):
                            cmd = commands.CompressFileZip(source = command_output, target= command_output[0][0:command_output[0].rfind("/")]+'/out.zip')
                        else: cmd = commands.CompressFileZip(source = command_output, target= command_output[0][0:command_output[0].rfind("/")]+'/'+bt.widget.ids.name.text+'.zip')
                        cmd_runner = commands.CommandRunner(cmd.build())
                        cmd_runner.start()
                        cmd_runner.join()
                        print(cmd_runner.output)
                        command_output = ['/tmp/xx.zip']
                    elif bt.widget.ids.type.text == '.XZip':
                        print('ss')
                        if(bt.widget.ids.name.text == ''):
                            cmd = commands.CompressFileZip(source = command_output, target= command_output[0][0:command_output[0].rfind("/")]+'/out.xzip')
                        else: cmd = commands.CompressFileZip(source = command_output, target= command_output[0][0:command_output[0].rfind("/")]+'/'+bt.widget.ids.name.text+'.xzip')
                        print('XZip')
                
                elif bt.widget.__class__.__name__ == 'HiddenFile':
                    print('hiddenfile')
                
                elif bt.widget.__class__.__name__ == 'ConvertPDFFile':
                    print(bt.widget.ids.type.text)
                    if bt.widget.ids.type.text == 'image to PDF':
                        print("command_output:",command_output)
                        cmd = commands.PDFMergging(source=command_output, target= path_file+'/'+bt.widget.ids.nameinput.text+'.pdf')
                        cmd_runner = commands.CommandRunner(cmd.build())
                        cmd_runner.start()
                        cmd_runner.join()
                        command_output = [path_file+'/'+bt.widget.ids.nameinput.text+'.pdf']
                        print(command_output)
                elif bt.widget.__class__.__name__ == 'ResizeImage':
                    print(bt.widget.ids.size_per.text)
                    if type(command_output) is list:
                            for i in command_output:
                                cmd = commands.Resize(source = i, percent= str(bt.widget.ids.size_per.text)+'%' ,target=i[:i.rfind('.')]+str(bt.widget.ids.type_name.text))
                                cmd_runner = commands.CommandRunner(cmd.build())
                                cmd_runner.start()
                                cmd_runner.join()
                                print('this')
                                print(cmd_runner.output)
                                command_output = cmd_runner.output
#                 elif bt.widget.__class__.__name__ == 'AddPhotoToAlbum':
#                     if type(command_output) is list:
#                             for i in command_output:
#                                 cmd = commands.resize(source = i, target=i[:i.rfind('.')]+".jpg")
#                                 cmd_runner = commands.CommandRunner(cmd.build())
#                                 cmd_runner.start()
#                                 cmd_runner.join()
#                                 print(cmd_runner.output)
#                                 command_output = cmd_runner.output
                elif bt.widget.__class__.__name__ == 'ChangeImageType':

                    for i in command_output:
                        cmd = commands.ChangImageTypeCommand(source = i, target=i[:i.rfind('.')] + bt.widget.ids.type.text)
                        cmd_runner = commands.CommandRunner(cmd.build())
                        cmd_runner.start()
                        cmd_runner.join()
                        print(cmd_runner.output)
                                
                elif bt.widget.__class__.__name__ == 'ConvertMusicType':
                    print("command_output:",command_output)

                    print(bt.widget.ids.type.text)
                    output = []
                    for i in command_output:
                        cmd = commands.ConvertMusicFile(source = i[:i.rfind('.')]+ str(bt.widget.ids.type.text), target = i)
                        cmd_runner = commands.CommandRunner(cmd.build())
                        cmd_runner.start()
                        cmd_runner.join()
                        output.append(i[:i.rfind('.')]+ str(bt.widget.ids.type.text))
                    command_output = output
                    print(command_output)
                 
                elif bt.widget.__class__.__name__ == 'ConvertVideoType':
                    print("command_output:",command_output)
                    print(bt.widget.ids.type.text)
                    output = []
                    for i in command_output:
                        cmd = commands.ConvertVideoFile(source = i , target = i[:i.rfind('.')]+ str(bt.widget.ids.type.text))
                        cmd_runner = commands.CommandRunner(cmd.build())
                        cmd_runner.start()
                        cmd_runner.join()
#                         output.append(i[:i.rfind('.')]+ str(bt.widget.ids.type.text))
                    command_output = output
                    print(command_output)
                                
#                 elif bt.widget.__class__.__name__ == 'ConvertMusicType':
#                     print("command_output:",command_output)
#                     cmd = commands.ConvertMusicCommands(source = command_output, target="/tmp/out.wav")
#                     cmd_runner = commands.CommandRunner(cmd.build())
#                     cmd_runner.start()
#                     cmd_runner.join()
#                     command_output = cmd_runner.output
#                     print(cmd_runner.output)
#                     command_output = ['/tmp/out.wav']
#                     print(cmd_runner.output)

            self.complete.open()
                
#                                 command_output = cmd_runner.output
                        
                        ##subprocess.call(['convert','*.png',str(bt.widget.ids.nameinput.text+'.pdf')])
#1                     os.system('ls '+str(path_file))
#                 elif bt.widget.__class__.__name__ == 'NewFolder':
# #                     print((bt.widget.ids.text_folder.text))
#                     subprocess.call(["mkdir", str(bt.widget.ids.text_folder.text)])
#                     subprocess.call(['ls'])
                                  
#     def on_touch_down(self, touch):
#         super().on_touch_down(touch)
#         
#         if self.ids.play_button.enable%2 == 0:
#             self.ids.play_button.background_normal = '../sdcn/data/images/play1.png'
#             self.ids.play_button.background_down = '../sdcn/data/images/pause1.png'
#         else:
#             self.ids.play_button.background_normal = 'pause1.png'
#             self.ids.play_button.background_down = 'play1.png'
#             self.ids.play_button.background_normal = '../sdcn/data/images/pause1.png'
#             self.ids.play_button.background_down = '../sdcn/data/images/play1.png'
            
    def change_submenu(self, menu_name, button):
        for bt in self.main_menu_layout.children:
            if bt.disabled == True :
                bt.disabled = False
        button.disabled = True
            
        for submenu in self.submenus:
            if submenu.__class__.__name__ == menu_name:
                sound = SoundLoader.load('../sdcn/data/audio/button.wav')
                sound.play()
                self.sub_menu_layout.clear_widgets()
                self.sub_menu_layout.add_widget(submenu)
                break
            
    def save_workflow(self):
        save_popup = SavePopup(title = 'Save',workflow_layout = self.workflow_layout)
        save_popup.open()

    def open_workflow(self):
        open_popup = OpenPopup(title = 'Open',workflow_layout = self.workflow_layout,main_menu_layout = self.main_menu_layout)
        open_popup.open()
#         workflow_file = None
#         with open('/tmp/work_flow.json', 'r') as f:
#             workflow_file = json.load(f, workflow_file)
#         f.close()
#     
#         self.workflow_layout.clear_widgets()
#         submenu = SubMenu(self.workflow_layout, self.main_menu_layout)
#         for wf_dict in workflow_file['workflow']:
#             if wf_dict['name'] == "Find File":
#                 dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
#                 widget = dw.widget
#                 widget.ids.path_input.text = wf_dict['path_file']
#                 widget.ids.file_input.text = wf_dict['pattern']
#             elif wf_dict['name'] == "Convert PDF File":
#                 dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
#                 widget = dw.widget
#                 widget.ids.type.text = wf_dict['type']
#                 widget.ids.nameinput.text = wf_dict['target']

