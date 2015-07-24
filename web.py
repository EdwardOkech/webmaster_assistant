import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar

Builder.load_string('''
<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Webmaster Manager Tool'
    Button:
        text: 'Welcome to Webmaster Manager Tool'
        on_press: root.dismiss()



<ProgressBar>:
    value: (20 * root.value) % (1 + self.max)
    size_hint_y: None
    height: 50


''')



class CustomPopup(Popup):
    pass


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.cols = 2
        self.add_widget(Label(text='User Name:'))
        self.username = TextInput(multiline =False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)

class MyApp(App):
    def build(self):
        b = Button(on_press=self.show_popup)
        return LoginScreen()

    def show_popup(self, b):
        p = CustomPopup()
        p.open()

if __name__ == '__main__':
    MyApp().run()
