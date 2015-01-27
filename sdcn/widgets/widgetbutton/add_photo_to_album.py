'''
Created on Jan 27, 2015

@author: progreanmer
'''
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
import os
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.button import Button
Builder.load_file(os.path.dirname(__file__) + '/add_photo_to_album.kv')
class AddPhotoToAlbum(StackLayout):
    def open_file_chooser(self):
        popup_filechoser = Popup(title = 'AddPhotoToAlbum')
        filechoser_layout = StackLayout(orientation = "lr-bt")
        filechoser = FileChooserListView(size_hint = (0.75,1),size = (1,400))
        ok_button = Button(text = 'Ok',size_hint=(0.12,None),size = (1,25))
        cancel_button = Button( text = 'Cancel',size_hint = (0.12,None), size=(1,25))
        filechoser_layout.add_widget(filechoser)
        filechoser_layout.add_widget(ok_button)
        filechoser_layout.add_widget(cancel_button)
        popup_filechoser.add_widget(filechoser_layout)
        popup_filechoser.open()
        cancel_button.bind(on_press = popup_filechoser.dismiss)
        
class TestApp(App):
     def build(self):
         return AddPhotoToAlbum()
 
if __name__ == '__main__':
     TestApp().run()
     