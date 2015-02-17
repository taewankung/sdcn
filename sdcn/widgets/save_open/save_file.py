'''
Created on Feb 10, 2015

@author: taewankung
'''
from kivy.app import App
from sdcn.widgets.widgetbutton.my_filechooser import MyFilechooser
from kivy.lang import Builder
from kivy.uix.popup import Popup
import json
Builder.load_string("""
<SavePopup>:
    StackLayout:
        orientation: 'tb-lr'
        FileChooserIconView:
            id: save_filechooser
            size_hint: (1,0.9)
            path:'/home'
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
    def ok_path(self):
        workflow=[]
  
        for wf_widget in reversed(self.workflow_layout.children):
            wf = dict()
            if wf_widget.widget.ids.workflow_header.text == 'Find File':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          path_file = wf_widget.widget.ids.path_input.text,
                          pattern = wf_widget.widget.ids.file_input.text
                        )
            elif wf_widget.widget.ids.workflow_header.text == 'Convert PDF File':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                          target = wf_widget.widget.ids.nameinput.text
                        )
                           
            elif wf_widget.widget.ids.workflow_header.text == 'Convert Music Type':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
                          target = wf_widget.widget.ids.nameinput.text
                        )
                
                           
            elif wf_widget.widget.ids.workflow_header.text == 'Convert Video Type':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                         type = wf_widget.widget.ids.type.text,
                         target = wf_widget.widget.ids.nameinput.text
                        )
                           
            elif wf_widget.widget.ids.workflow_header.text == 'Compress Files':
                wf = dict(name=wf_widget.widget.ids.workflow_header.text ,
                          type = wf_widget.widget.ids.type.text,
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
                pass
                              
            workflow.append(wf)
        workflow_file = dict(workflow=workflow)
        if(str(self.ids.save_filechooser.path) != ''):
            with open(str(self.ids.save_filechooser.path)+'/'+self.ids.name.text+'.json', 'w') as f:
                json.dump(workflow_file, f)
            f.close()            
            workflow_file = dict(workflow=workflow)
        self.dismiss()
# class TestApp(App):
#      def build(self):
#          return SavePopup(title = 'save file')
#  
# if __name__ == '__main__':
#      TestApp().run()