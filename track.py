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
    def __init__(self, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        sound_button = TrackSoundButton()
        sound_button.text = "nom du son"
        self.add_widget(sound_button)  # ajout nom du soundkit
        for i in range(0, TRACK_NB_STEPS):  # ajout des stepbutton
            self.add_widget(TrackStepButton())
