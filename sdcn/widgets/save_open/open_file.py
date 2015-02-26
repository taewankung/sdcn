'''
Created on Feb 11, 2015

@author: aran
'''
from kivy.app import App
from sdcn.widgets.widgetbutton.my_filechooser import MyFilechooser
from kivy.lang import Builder
from kivy.uix.popup import Popup
import json
from sdcn.widgets.submenu.submenu import SubMenu
from os.path import expanduser
Builder.load_string("""
<OpenPopup>:
    StackLayout:
        orientation: 'tb-lr'
        FileChooserIconView:
            id: open_chooser
            size_hint: (1,0.9)
        BoxLayout:
            size_hint: (1,0.09)
            Label:
                text: 'Name'
                size_hint: (0.24,0.5)
            TextInput:
                id: name
                size_hint: (0.75,None)
                size: (100,50)
                font_size: 20
            Button:
                id: _ok
                text: 'Ok'
                size_hint: (None,None)
                size: (100,50)
                on_press: root.okfile()
            Button:
                id: _cancel
                text: 'Cancel'
                size_hint: (None,None)
                size: (100,50)
                on_press: root.dismiss()
""")
class OpenPopup(Popup):
    def __init__(self, title, workflow_layout, main_menu_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
        self.main_menu_layout = main_menu_layout
        self.ids.open_chooser.path = expanduser("~")
    def okfile(self):
        workflow_file = None
        with open(self.ids.open_chooser.selection[0], 'r') as f:
            workflow_file = json.load(f, workflow_file)
        f.close()
    
        self.workflow_layout.clear_widgets()
        submenu = SubMenu(self.workflow_layout, self.main_menu_layout)
        for wf_dict in workflow_file['workflow']:
            
            if wf_dict['name'] == "Find File":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.path_input.text = wf_dict['path_file']
                widget.popup_filechoser.filechooser.path = widget.ids.path_input.text
                widget.ids.file_input.text = wf_dict['pattern']
            elif wf_dict['name'] == "Compress Files":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type.text = wf_dict['type']
                widget.ids.output_name.text = wf_dict['output_name']
            elif wf_dict['name'] == "Hidden Files":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
            elif wf_dict['name'] == "New Folder":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.text_folder.text = wf_dict['text_folder']
            elif wf_dict['name'] == "Change Image Type":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type.text = wf_dict['type']
            elif wf_dict['name'] == "Resize Image":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type_name.text = wf_dict['type_name']
                widget.ids.size_per.text = wf_dict['size_per']
            elif wf_dict['name'] == "Rename Image":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.name_input.text = wf_dict['name_input']
            elif wf_dict['name'] == "Rotate Image":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.name_input.text = wf_dict['name_input']
                widget.ids.degree.text = wf_dict['degree']
            elif wf_dict['name'] == "Convert PDF File":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type.text = wf_dict['type']
                widget.ids.nameinput.text = wf_dict['target']
            elif wf_dict['name'] == "Convert Music Type":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type.text = wf_dict['type']
                widget.ids.nameinput.text = wf_dict['target']
            elif wf_dict['name'] == "Convert Video Type":
                dw = submenu.add_widget_to_workflow_layout(wf_dict['name'])
                widget = dw.widget
                widget.ids.type.text = wf_dict['type']
                widget.ids.nameinput.text = wf_dict['target']
            
        self.dismiss()
        
