from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.relativelayout import RelativeLayout
from model.sound_kit_service import SoundKitService
from track import TrackWidget

Builder.load_file("track.kv")  # integration du track.kv dans fenetre principale (+voir mrbeat.kv)


class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()

    def on_parent(self, widget, parent):
        """on_parent attend que l'app soit instanciee pour continuer"""
        nb_tracks = self.sound_kit_service.get_nb_tracks()
        for i in range(0, nb_tracks):
            self.tracks_layout.add_widget(TrackWidget())



class MrBeatApp(App):
    pass


MrBeatApp().run()
