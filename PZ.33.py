from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout


class myApp(App):
    def build(self):
        s=AnchorLayout()
        fl = BoxLayout(orientation = 'vertical', size_hint = [.50,.50], spacing=60)

        fl.add_widget(Button(
            text="Здравствуйте,",
            font_size=20,
            on_press=self.btn_press,
            background_color=[.65,.20,.40,1],         
            background_normal=''))


        fl.add_widget(Button(
             text="Ирина Сергеевна!",
            font_size=20,
            on_press=self.btn_press,
            background_color=[1.62,.30,.80,1],
            background_normal=''))

        s.add_widget(fl)
        return s
    def btn_press(self, instance):
        instance.text='Я нажата'

if __name__=="__main__":
    myApp().run()
