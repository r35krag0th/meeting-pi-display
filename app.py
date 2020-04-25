#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
from datetime import datetime, timedelta

from kivy.core.window import Window
Window.fullscreen = 'auto'

class MDCoreLayout(BoxLayout):
    # This is "PongGame"
    current_month = ObjectProperty(None)
    current_day = ObjectProperty(None)

    def update_current_datetime(self):
        now = datetime.now()

        self.current_month = now.strftime('%B')
        self.current_day = now.strftime('%d')

    def update(self, dt):
        self.update_current_datetime()


class MeetingDisplayCore(Widget):
    # This is "PongGame"
    current_month = ObjectProperty(None)
    current_day = ObjectProperty(None)

    def update_current_datetime(self):
        now = datetime.now()

        self.current_month = now.strftime('%B')
        self.current_day = now.strftime('%d')

    def update(self, dt):
        self.update_current_datetime()


class MeetingDisplayApp(App):
    def build(self):
        core = MDCoreLayout()
        core.update_current_datetime()
        Clock.schedule_interval(core.update, 1.0)
        return core
        # return MDCoreLayout()

if __name__ == '__main__':
    MeetingDisplayApp().run()
