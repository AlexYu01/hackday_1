from kivy.app import App
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.properties import ObjectProperty, NumericProperty
from kivy.config import Config
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
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


class CountDown(Label):
    anim = None
    time_counter = NumericProperty(20)

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(time_counter=0, duration=self.time_counter)
        self.anim.start(self)


class Mode(Screen):

    def change_screen(self, count_down):
        self.manager.current = 'clicker'
        self.manager.ids.click_away.count = CountDown()
        self.manager.ids.click_away.count.time_counter = count_down
        self.manager.ids.click_away.count.start()


class ClickAway(Screen):
    addButton = ObjectProperty()
    countDown = ObjectProperty()
    count = None

    def __init__(self, **kwargs):
        super(ClickAway, self).__init__(**kwargs)
        self.count = CountDown()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, *args):
        self.countDown.text = str(round(self.count.time_counter, 1))

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