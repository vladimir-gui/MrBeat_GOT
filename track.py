from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

TRACK_NB_STEPS = 16


class TrackStepButton(ToggleButton):
    pass


class TrackSoundButton(Button):
    pass


class TrackWidget(BoxLayout):
    """ structure d'un track """
    def __init__(self, sound, audio_engine, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        sound_button.on_press = self.on_sound_button_press
        self.audio_engine = audio_engine
        self.sound = sound
        self.add_widget(sound_button)  # ajout nom du soundkit
        for i in range(0, TRACK_NB_STEPS):  # ajout des stepbutton
            step_button = TrackStepButton()
            self.add_widget(TrackStepButton())

    def on_sound_button_press(self):
        self.audio_engine.play_sound(self.sound.samples)
        print("sound !")

#     si clic sur bouton step button on realise un fonction qui genere un un tableau (tuple)
