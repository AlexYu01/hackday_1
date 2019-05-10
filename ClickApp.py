from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'resizable', False)
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class AddButton(Button):
    pass

class EasyButton(Button):
    pass

class NormalButton(Button):
    pass

class HardButton(Button):
    pass

class Mode(Screen):

    def change_screen(self, count_down):
        self.manager.current = 'clicker'
        self.manager.ids.click_away.timer = count_down

class ClickAway(Screen):
    addButton = ObjectProperty()
    timer = 0

    def add_one(self):
        value = int(self.addButton.text)
        self.addButton.text = str(value + 1)

    def enable(self):
        self.addButton.disabled = False

class Manager(ScreenManager):

    mode_screen = ObjectProperty(None)
    click_away = ObjectProperty(None)

class ClickApp(App):
    def build(self):
        self.title = 'Away ISA!'
        screen_manager = Manager(transition=SlideTransition())
        return screen_manager

if __name__ == "__main__":
    app = ClickApp()
    app.run()
