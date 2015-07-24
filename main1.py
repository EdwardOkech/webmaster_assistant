
import kivy
kivy.require('1.7.2')

from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string('''
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

class Main(GridLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        
        self.cols=2
        self.add_widget(Button(text='Log-in',on_press=self.login_screen))
        self.add_widget(Button(text='My Account'))
        self.add_widget(Button(text='News & Events'))
        self.add_widget(Button(text='Jobs'))

    def login_screen(self,state):
        self.cols = 2
        self.add_widget(Label(text='User Name:'))
        self.username = TextInput(multiline =False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)


class TestApp(App):
    def build(self):
        return Main()

    

TestApp().run()
