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
Builder.load_string('''
<Delete_button>
    text: 'X'
    size_hint: (0.1,0.3)
''')

        
class SubMenu(StackLayout):
    
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.bh = int(.075*self.workflow_layout.height)   
    def add_to_workflow_layout(self, button):
        new_label = Label(text=button.text, size_hint_x=0.89,
                            size_hint_y=0.5,background_color = (1,0,0,2))
        layout = StackLayout(size_hint = (1,None),size = (self.workflow_layout.width,self.bh*2))
#         layout.add_widget(Delete_button())
        if new_label.text == 'Find File':
            layout.add_widget(FindFile())
        elif new_label.text == 'Compress Files':
            typeFile = Spinner(text='.Zip',values=('.Zip','.XZip'),size_hint=(1,None),size=(1,44))
            layout.add_widget(typeFile)
        elif new_label.text == 'Convert Files':
            typeFile = Spinner(text='.doc to text',values=('.doc to text', '.doc to html'),size_hint=(1,None),size=(1,44))
            layout.add_widget(typeFile)
        elif new_label.text == 'New Folder':
            text_input_name = TextInput(multiline = False,size_hint = (0.5,None),size = (100,self.bh))
            label_text_name = Label(text = 'Name:',size_hint = (0.5,None), size = (100,self.bh))
            layout.add_widget(label_text_name)
            layout.add_widget(text_input_name)
#Picture Menu*****************************************************************************************************************************          PICTURE

        elif new_label.text == 'Resize Photo': 
            text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,25))
            l = Label(text='Example: ....', font_size='15sp', size_hint_y=None)
            l.bind(width=lambda s, w:
            s.setter('text_size')(s, (w, None)))
            l.bind(texture_size=l.setter('size'))
            layout.add_widget(text_input)
            layout.add_widget(l)
        
        elif new_label.text == 'Rename File':
            text_input = TextInput(text='', multiline = False , size_hint = (None,None), size = (100,self.bh))
            l = Label(text='Example: ....', font_size='15sp', size_hint_y = None)
            l.bind(width=lambda s, w:
            s.setter('text_size')(s, (w, None)))
            l.bind(texture_size=l.setter('size'))
            layout.add_widget(text_input)
            layout.add_widget(l)
        
        elif new_label.text == 'Add Photo To Album':
            filechoser_layout = StackLayout( orientation="lr-bt")
            filechoser = FileChooserListView( size_hint = (0.75,1), size=(1,400))
            filechoser_layout.add_widget(filechoser)
            ok_button = Button(text = 'Ok' , size_hint = (0.12,None), size=(1,25))
            cancel_button = Button(text = 'Cancel' ,size_hint = (0.12,None), size=(1,25))
            filechoser_layout.add_widget(ok_button)
            filechoser_layout.add_widget(cancel_button)
            browser_button = Button(text = 'Browser', size_hint = (0.5,None),size = (1, self.bh))
            popup_browser = Popup(title = 'Album')
            popup_browser.add_widget(filechoser_layout)
            cancel_button.bind(on_press = popup_browser.dismiss)
            browser_button.bind(on_press = popup_browser.open)
            input_file = TextInput(text = 'Directory file',size_hint = (0.5,None),size = (1, self.bh))
            layout.add_widget(browser_button)
            layout.add_widget(input_file)
            pass
        elif new_label.text == 'Crop Image':
            label_x = Label(text = 'X:',size_hint=(0.25,None), size = (100,self.bh))
            text_input_x = TextInput(size_hint=(0.24,None), size = (100,self.bh))
            label_y = Label(text = 'y:',size_hint=(0.25,None), size = (100,self.bh))
            text_input_y= TextInput(size_hint=(0.24,None), size = (100,self.bh))
            layout.add_widget(label_x)
            layout.add_widget(text_input_x)
            layout.add_widget(label_y)
            layout.add_widget(text_input_y)
        elif new_label.text == 'Change File Type':
            change_file_type = Spinner(text='.jpg',values=('.png', '.gif','.tif'),size_hint=(1,None),size=(1,44))
            layout.add_widget(change_file_type)
#END PIC*******************************************************************************************************************************END PIC
        
        elif new_label.text == 'Write File': 
            pass
        elif new_label.text == 'Add File':
            pass
        
#END FILE*******************************************************************************************************************************END FILE
        elif new_label.text == 'Convert PDF file':
            new_convert = ConvertPDFFile(self.workflow_layout)
            layout.add_widget(new_convert)
            pass
#END PDF********************************************************************************************************************************END PDF
        elif new_label.text == 'Convert Music Files':
            change_file_music_type = Spinner(text='.mp3 to .wav',values=('.mp3 to .wav','.wav to.mp3','.mp4 to .mp3','.ra to .mp3','.mp3 to .ra','.mp3 to .au'),size_hint=(1,None),size=(1,44))
            layout.add_widget(change_file_music_type)
            pass
#END MUSIC******************************************************************************************************************************END MUSIC
        elif new_label.text == 'Convert Video Files':
            change_file_video_type = Spinner(text='.dat to .mp4',values=('.dat to .mp4','.mp4 to .dat'),size_hint=(1,None),size=(1,44))
            layout.add_widget(change_file_video_type)
        elif new_label.text == 'Resize Video':
            label_x = Label(text = 'X:',size_hint=(0.25,None), size = (100,self.bh))
            text_input_x = TextInput(size_hint=(0.24,None), size = (100,self.bh))
            label_y = Label(text = 'y:',size_hint=(0.25,None), size = (100,self.bh))
            text_input_y= TextInput(size_hint=(0.24,None), size = (100,self.bh))
            layout.add_widget(label_x)
            layout.add_widget(text_input_x)
            layout.add_widget(label_y)
            layout.add_widget(text_input_y)    
#END Video******************************************************************************************************************************END Video
        self.workflow_layout.add_widget(layout)
    def delete_(self, button):
        pass
