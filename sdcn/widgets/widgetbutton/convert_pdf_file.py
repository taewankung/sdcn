from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
from sdcn.widgets.widgetbutton.deleteable import WorkflowWidget
Builder.load_file(os.path.dirname(__file__) + '/convert_pdf_file.kv')
class ConvertPDFFile(WorkflowWidget):
    def __init__(self, workflow_layout):
        super().__init__(workflow_layout)

# class TestApp(App):
#     def build(self):
#         return Convert_PDF_file()
# 
# if __name__ == '__main__':
#     TestApp().run()
#     