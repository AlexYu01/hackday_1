from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout


class AddButton(Button):
    pass


class Container(GridLayout):
    addButton = ObjectProperty()

    def add_one(self):
        value = int(self.addButton.text)
        self.addButton.text = str(value + 1)


class ClickApp(App):
    def build(self):
        self.title = 'Away ISA!'
        return Container()


if __name__ == "__main__":
    app = ClickApp()
    app.run()
