"""
This is a replica of the flutter example counter app.
Note that there are many ways of implementing this app,
I just wanted to go with the most basic and simplified way
I could find.

Author : Tobias HT
Email : higenyi.tobias@gamil.com
twitter: TobiasHT5
"""
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel

class CounterApp (MDApp):
    
    def __init__(self):
        super(CounterApp,self).__init__()
        self.view = MDBoxLayout(orientation = "vertical")
        self.view_widgetset = MDFloatLayout()
        self.add_button = MDFloatingActionButton(icon = "plus",
                                                on_release = self.add_action,
                                                pos_hint = {"x":0.9, "y":0.1}
                                                )
        self.text = MDLabel(text = "You have pushed the button this many times:",
                            pos_hint = {"center_x":0.5,"center_y":0.7},
                            halign = "center",
                            font_style = "Subtitle1"
                            )
        self.value_text = MDLabel(text = "0",
                            pos_hint = {"center_x":0.5,"center_y":0.6},
                            font_style = "H4",
                            halign = "center"
                            )
        self.value = 0
    
    def add_action (self,inst):
        self.value += 1
        self.value_text.text = str(self.value)
        
    def build (self):
        toolbar = MDToolbar(title = "KivyMD Demo Home Page")
        self.view.add_widget(toolbar)
        self.view.add_widget(self.view_widgetset)
        self.view_widgetset.add_widget(self.text)
        self.view_widgetset.add_widget(self.value_text)
        self.view_widgetset.add_widget(self.add_button)
        return self.view
        
        
CounterApp().run()