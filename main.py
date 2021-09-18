from kivy.app import App
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout

Builder.load_file("track.kv")  # integration du track.kv dans fenetre principale (+voir mrbeat.kv)

NB_TRACKS = 4


class MainWidget(RelativeLayout):
    def on_parent(self, widget, parent):
        """on_parent attend que l'app soit instanciee pour continuer"""
        pass


class MrBeatApp(App):
    pass


MrBeatApp().run()
