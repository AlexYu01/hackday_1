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


#class Timer():
#    def build(self):
#        self.modes = ('%S:')
#        self.mode = 0
#        self.main_box = BoxLayout(orientation='vertical')
#        
#        self.button = Button(text='label', font_size=100)
#        self.main_box.add_widget(self.button)
#    
#        self.button.bind(on_press=self.tap)
#        Clock.schedule_interval(self.timer, 0.01)
#        
#        return self.main_box
#    
#    def tap(self, button):
#        if self.mode +1 == len(self.modes):
#            self.mode = 0
#        else:
#            self.mode +=1
#    
#    def timer(self, dt):
#        now = datetime.datetime.now()
#        self.button.text = now.strftime(self.modes[self.mode])
#        if self.mode == 2:
#            self.button.text += str(now.microsecond)[:3]

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
