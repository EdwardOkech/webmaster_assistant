# -*- coding: utf-8 -*-

import kivy
kivy.require('1.7.2')

from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.accordion import Accordion, AccordionItem



Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

<MenuScreen>:
    GridLayout:
        cols: 2
        padding:2,2
        spacing:5
        Button:
            
            background_color: 0,0,1,0
            text: 'Log-in'
            font_name:'data/fonts/Roboto-Thin.ttf'
            on_press: root.manager.current = 'login'
            on_press:root.manager.transition = FadeTransition()
            Image:
                source:'res/tl.png'
                pos:self.parent.pos
                size:self.parent.size
                allow_stretch: 1
                keep_ratio:0
            
            
        Button:
            background_color:1,1,1,0
            text: 'My Account'
            on_press: root.manager.current = 'account'
            on_press:root.manager.transition = FadeTransition()
            Image:
                source:'res/tr.png'
                pos:self.parent.pos
                size:self.parent.size
                allow_stretch: 1
                keep_ratio:0
        Button:
            background_color:1,1,1,0
            text: 'News & Events'
            on_press: root.manager.current = 'news'
            on_press:root.manager.transition = FadeTransition()
            Image:
                source:'res/bl.png'
                pos:self.parent.pos
                size:self.parent.size
                allow_stretch: 1
                keep_ratio:0
        Button:
            background_color:1,1,1,0
            text: 'Jobs'
            Image:
                source:'res/br.png'
                pos:self.parent.pos
                size:self.parent.size
                allow_stretch: 1
                keep_ratio:0

<LoginScreen>:
    BoxLayout:
        padding: 50,50
        orientation: 'vertical'
        Label:
            text: 'Username:'
        TextInput:
            text: 
                
        Label:
            text: 'Password:'
        TextInput:
            text: 
            password: True
            multiline: False   
        Button:
            text: 'back to menu'
            on_press: root.manager.current = 'menu'
            on_press:root.manager.transition = FadeTransition()

<MyAccount>:
    BoxLayout:
        padding: 50,50
        orientation: 'vertical'
        Accordion:
            orientation: 'vertical'
            AccordionItem:
                title: 'Maidea Creative Reality :(www.maidea.co.ke)'
                Label:
                    text: 'cpanel: maideaadmin'
                    text: 'password: 446rgfgfb'
                    text_size: self.width, None

            AccordionItem:
                title: 'Creative Circles Ltd :(www.creativecircle.co.ke)'
                    

            AccordionItem:
                title: 'Heart 2 Heart Project :(www.heart2heartproject.org)'
                Label:
                    text: 'djfhkdflhkfjhk'
                    text_size: self.width, None

        Button:
            text: 'back to menu'
            on_press: root.manager.current = 'menu'
            on_press:root.manager.transition = FadeTransition()

<NewsEvents>:
    BoxLayout:
        padding: 50,50
        orientation: 'vertical'
        Button:
            text: 'news 1'
            on_press:root.show_popup()
        Button:
            text: 'back to menu'
            on_press: root.manager.current = 'menu'
            on_press:root.manager.transition = FadeTransition()
    
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Hello world'
    Button:
        text: 'Click me to dismiss'
        on_press: root.dismiss()

''')
class CustomPopup(Popup):
    pass
class MenuScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class MyAccount(Screen):
    pass
class NewsEvents(Screen):
    def show_popup(self):
        p = CustomPopup()
        p.open()
        

class Jobs(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MyAccount(name='account'))
sm.add_widget(NewsEvents(name='news'))

class ControllerApp(App):

    def build(self):
        return sm

    

if __name__ == '__main__':
    ControllerApp().run()


