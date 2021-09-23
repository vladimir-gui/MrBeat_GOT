from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.relativelayout import RelativeLayout

from audio_engine import AudioEngine
from model.sound_kit_service import SoundKitService
from track import TrackWidget

Builder.load_file("track.kv")  # integration du track.kv dans fenetre principale (+voir mrbeat.kv)
Builder.load_file("play_indicator.kv")  # integration du play_indicator.kv dans fenetre principale

TRACK_NB_STEPS = 16

# button play/stop
# hauteur dp(100)
# creer class custom controlbutton heritant de button

class MainWidget(RelativeLayout):
    tracks_layout = ObjectProperty()
    play_indicator_widget = ObjectProperty()
    TRACK_STEPS_LEFT_ALIGN = NumericProperty(dp(100))
    
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.sound_kit_service = SoundKitService()

        # kick_sound = self.sound_kit_service.get_song_at(0)

        self.audio_engine = AudioEngine()
        # self.audio_engine.play_sound(kick_sound.samples)  # kick au demarrage

        # self.audio_engine.create_track(kick_sound.samples, 120)
        self.audio_mixer = self.audio_engine.create_mixer(self.sound_kit_service.soundkit.get_all_samples(), 120, TRACK_NB_STEPS)

    def on_parent(self, widget, parent):
        """on_parent attend que l'app soit instanciee pour continuer"""
        self.play_indicator_widget.set_nb_steps(TRACK_NB_STEPS)
        nb_tracks = self.sound_kit_service.get_nb_tracks()
        for i in range(0, nb_tracks):
            sound = self.sound_kit_service.get_song_at(i)
            self.tracks_layout.add_widget(
                TrackWidget(
                    sound, self.audio_engine, TRACK_NB_STEPS, self.audio_mixer.tracks[i], self.TRACK_STEPS_LEFT_ALIGN
                )
            )


class MrBeatApp(App):
    pass


MrBeatApp().run()
