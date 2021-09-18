from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton

TRACK_NB_STEPS = 16


class TrackStepButton(ToggleButton):
    pass


class TrackWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        for i in range(0, TRACK_NB_STEPS):
            self.add_widget(TrackStepButton())
