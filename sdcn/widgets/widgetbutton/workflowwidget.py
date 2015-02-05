'''
Created on Jan 26, 2015

@author: aran
'''
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout


from sdcn.garden.magnet import Magnet
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock


class WorkflowWidget(StackLayout):
    def __init__(self, workflow_layout):
        super().__init__()
        self.workflow_layout = workflow_layout
    
    def delete_in_workflow_layout(self, menu): 
        for c in self.workflow_layout.children:
            if c.widget == menu:
                self.workflow_layout.remove_widget(c)
        

class DraggableWidgetContainer(Magnet):
    widget = ObjectProperty(None, allownone=True)
    workflow_layout = ObjectProperty(None)
    main_layout = ObjectProperty(None)

    def on_widget(self, *args):
        self.clear_widgets()

        if self.widget:
            Clock.schedule_once(lambda *x: self.add_widget(self.widget), 0)

    def on_touch_down(self, touch, *args):

        if "scroll" in touch.button:
            return super().on_touch_down(touch, *args)
        
        if self.widget.ids.workflow_header.collide_point(*touch.pos):
            touch.grab(self)
            self.remove_widget(self.widget)
#             print(touch.pos)
            # self.app.root.add_widget(self.widget)
            self.center = touch.pos
            self.widget.center = touch.pos
#             print(self.widget.pos)
            self.main_layout.add_widget(self.widget)
#             self.widget.pos = (100,100)
#             print(self.widget.pos)
            return True

        return super().on_touch_down(touch, *args)

    def on_touch_move(self, touch, *args):

        if touch.grab_current == self:
            self.widget.center = touch.pos
            self.widget.pos = touch.pos
            if self.workflow_layout.collide_point(*touch.pos):
                
                self.workflow_layout.remove_widget(self)
                #float_layout.remove_widget(self)
                #print(self.workflow_layout.children)

                for i, c in enumerate(self.workflow_layout.children):
#                     print(c.children)
                    if c.collide_point(*touch.pos):
                        #print(i, c)
                        #print("add:", i+1)
                        self.workflow_layout.add_widget(self, i+1)
                        break
                else:
                    #print("not")
                    self.workflow_layout.add_widget(self)
            else:
                #print("notnot")
                if self.parent == self.workflow_layout:
                    #self.workflow_layout.remove_widget(self)
                    #float_layout.add_widget(self)
                    pass

                self.center = touch.pos

        return super().on_touch_move(touch, *args)

    def on_touch_up(self, touch, *args):

        
        if "scroll" in touch.button:
            return super().on_touch_up(touch, *args)
        
        if touch.grab_current == self:
            #self.app.root.remove_widget(self.widget)
            self.main_layout.remove_widget(self.widget)
#             if self not in self.workflow_layout.children:
#                 self.workflow_layout.add_widget(self)
            self.add_widget(self.widget)
            touch.ungrab(self)
            self.workflow_layout.do_layout()
            return True

        return super().on_touch_up(touch, *args)
