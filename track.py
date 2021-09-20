from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

TRACK_NB_STEPS = 16


class TrackStepButton(ToggleButton):
    pass


class SoundKitButton(Button):
    pass


class TrackWidget(BoxLayout):
    """ structure d'un track """
    def __init__(self, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        self.add_widget(SoundKitButton())  # ajout nom du soundkit
        for i in range(0, TRACK_NB_STEPS):  # ajout des stepbutton
            self.add_widget(TrackStepButton())
