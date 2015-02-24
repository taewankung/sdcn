'''
Created on Feb 10, 2015

@author: taewankung
'''
from kivy.app import App
from sdcn.widgets.widgetbutton.my_filechooser import MyFilechooser
from kivy.lang import Builder
from kivy.uix.popup import Popup
import json
import subprocess
from os.path import expanduser
Builder.load_string("""
<SavePopup>:
    StackLayout:
        orientation: 'tb-lr'
        FileChooserIconView:
            id: save_filechooser
            size_hint: (1,0.9)
        BoxLayout:
            size_hint: (1,0.09)
            Label:
                text: 'Name'
                size_hint: (0.24,0.5)
            TextInput:
                id: name
                size_hint: (0.75,0.75)
            Button:
                id: _ok
                text: 'Ok'
                size_hint: (None,None)
                size: (100,25)
                on_press: root.ok_path()
            Button:
                id: _cancel
                text: 'Cancel'
                size_hint: (None,None)
                size: (100,25)
                on_press: root.dismiss()
        
""")
class SavePopup(Popup):
    def __init__(self,title,workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.title = title
        self.ids.save_filechooser.path = expanduser("~")
    def ok_path(self):
        workflow=[]
  
        for wf_widget in reversed(self.workflow_layout.children):
            wf = dict()
            if wf_widget.widget.ids.workflow_header.text == 'Find File':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          path_file = wf_widget.widget.ids.path_input.text,
                          pattern = wf_widget.widget.ids.file_input.text
                        )           
            elif wf_widget.widget.ids.workflow_header.text == 'Convert Music Type':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                          target = wf_widget.widget.ids.nameinput.text
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Convert PDF File':
                 wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                          target = wf_widget.widget.ids.nameinput.text
                        )                           
            elif wf_widget.widget.ids.workflow_header.text == 'Convert Video Type':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                         type = wf_widget.widget.ids.type.text,
                         target = wf_widget.widget.ids.nameinput.text
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Convert Files':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                         type = wf_widget.widget.ids.type.text,
                        )
                              
            elif wf_widget.widget.ids.workflow_header.text == 'Compress Files':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                          output_name = wf_widget.widget.ids.output_name.text
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Hidden Files':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'New Folder':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          text_folder = wf_widget.widget.ids.text_folder.text
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Change Image Type':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                        )
            
            elif wf_widget.widget.ids.workflow_header.text == 'Resize Image':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type_name = wf_widget.widget.ids.type_name.text,
                          size_per = wf_widget.widget.ids.size_per.text,
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Rename Image':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          name_input = wf_widget.widget.ids.name_input.text,
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Rotate Image':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          degree = wf_widget.widget.ids.degree.text,
                          name_input = wf_widget.widget.ids.name_input.text
                        )                 
            workflow.append(wf)
        workflow_file = dict(workflow = workflow)
        if(str(self.ids.save_filechooser.path) != '~/' and str(self.ids.save_filechooser.path) != ''):
            with open(str(self.ids.save_filechooser.path)+'/'+self.ids.name.text+'.json', 'w') as f:
                json.dump(workflow_file, f)
        elif str(self.ids.save_filechooser.path) == '~/':
            with open(str(self.ids.save_filechooser.path)+self.ids.name.text+'.json', 'w') as f:
                json.dump(workflow_file, f)
            f.close()            
            workflow_file = dict(workflow=workflow)
            print(self.ids.save_filechooser.path)
        
            
        self.dismiss()
# class TestApp(App):
#      def build(self):
#          return SavePopup(title = 'save file')
#  
# if __name__ == '__main__':
#      TestApp().run()
