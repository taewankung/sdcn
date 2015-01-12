'''
Created on Dec 26, 2014

@author: returner
'''


#standard ตัวเก็บพวกเมนูอะไรประมาณนี้
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class SdcnApplication(App):
    def build(self):
        App_layout = BoxLayout(orientation = 'vertical')
        logo_layout = StackLayout(orientation = 'tb-lr',size_hint = (0.2,0.2))
        logo = Image(source='logo.png')
        name = Image(source='name.png')
        logo_layout.add_widget(logo)
        logo_layout.add_widget(name)
        menu_type = StackLayout(orientation = 'tb-lr')
        standard = BoxLayout()
        
        menu = StackLayout(orientation = 'tb-lr')
        search_menu =  StackLayout(orientation = 'lr-tb',size_hint = (1,0.05))
        order = StackLayout(orientation = 'tb-lr')
        label_menu = Label(text = "Menu",size_hint=(1,0.075),font_size = 25)
        document = Button(text = "Document",size_hint=(1,0.075))
        picture = Button(text = "Picture",size_hint=(1,0.075))
        file_and_folder = Button(text = "File and folder",size_hint=(1,0.075))
        pdfs = Button(text = "PDF",size_hint=(1,0.075))
        menu_type.add_widget(label_menu)
        menu_type.add_widget(document)
        menu_type.add_widget(picture)
        menu_type.add_widget(file_and_folder)
        menu_type.add_widget(pdfs)
#       MENU
        search = TextInput(multiline = False , size_hint = (0.60,1) )
        label_search = Label(text = "Search",size_hint=(None,1),font_size = 20)
        search_menu.add_widget(label_search)
        search_menu.add_widget(search)
#        test_label = Button(text="xxx",background_color = (1,0,1,1),size_hint = (1,0.060))
#        test_label2 = Button(text="xxx",background_color = (1,0,1,1),size_hint = (1,0.060))
        menu.add_widget(search_menu)
#        order.add_widget(test_label)
#        order.add_widget(test_label2)
#        menu.add_widget(test_label2)
#       Add in starndard
        standard.add_widget(menu_type)
        standard.add_widget(menu)
        standard.add_widget(order)
        App_layout.add_widget(logo_layout)
        App_layout.add_widget(standard)
        return App_layout
#    function document*******************************************************************************
        document_menu = StackLayout(orientation = 'tb-lr')
        doc_find_file = Button( text = "Find file",size_hint=(1,0.075))
        document_menu.add_widget(doc_find_file)
        doc_to_text = Button( text = "doc to text",size_hint=(1,0.075))
        document_menu.add_widget(doc_to_text)
        doc_to_html = Button( text = "doc to html",size_hint=(1,0.075))
        document_menu.add_widget(doc_to_html)
        doc_compress_files = Button( text = "compress files",size_hint=(1,0.075))
        document_menu.add_widget(doc_compress_files)
#****************************************************************************************************