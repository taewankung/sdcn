# from kivy.uix.spinner import Spinner

# from kivy.uix.stacklayout import StackLayout

# from kivy.app import App
from kivy.lang import Builder
from sdcn.widgets.widgetbutton.deleteable import WorkflowWidget
import os
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