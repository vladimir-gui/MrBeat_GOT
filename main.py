from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file("track.kv")  # integration du track.kv dans fenetre principale (+voir mrbeat.kv)


class MainWidget(RelativeLayout):
    pass


class MrBeatApp(App):
    pass


MrBeatApp().run()
