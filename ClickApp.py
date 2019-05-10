from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)


class AddButton(Button):
    pass


class EasyButton(Button):
    pass


class NormalButton(Button):
    pass


class HardButton(Button):
    pass


class Container(Widget):
    addButton = ObjectProperty()

    def add_one(self):
        value = int(self.addButton.text)
        self.addButton.text = str(value + 1)

    def enable(self):
        self.addButton.disabled = False


class ClickApp(App):
    def build(self):
        self.title = 'Away ISA!'
        stuff = Container()
        stuff.addButton.disabled = True
        return stuff


if __name__ == "__main__":
    app = ClickApp()
    app.run()
