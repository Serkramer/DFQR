from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class MyApp(App):
    def build(self):
        fl = FloatLayout(size=(300, 300))
        fl.add_widget(Button(text="это моя первая кнопка",
                             font_size=15,
                             on_press=self.btn_press,
                             background_color=[255, 0, 0, 1],
                             size_hint=(.5, .25),
                             pos=(100, 250)))

        return fl

    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Кнопка нажата"


if __name__ == "__main__":
    MyApp().run()

