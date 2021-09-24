from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.togglebutton import ToggleButton


class TrackStepButton(ToggleButton):
    pass


class TrackSoundButton(Button):
    pass


class TrackWidget(BoxLayout):
    """ structure d'un track """
    def __init__(self, sound, audio_engine, nb_steps, track_source, steps_left_align, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)

        self.audio_engine = audio_engine
        self.sound = sound
        self.track_source = track_source

        # boxlayout button separator
        boxlayout_button_separator = BoxLayout()
        boxlayout_button_separator.size_hint_x = None
        boxlayout_button_separator.width = steps_left_align
        self.add_widget(boxlayout_button_separator)

        # sound_button
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        sound_button.on_press = self.on_sound_button_press
        boxlayout_button_separator.add_widget(sound_button)  # ajout nom du soundkit

        # separateur
        separator_image = Image(source="images/track_separator.png")
        separator_image.size_hint_x = None
        separator_image.width = dp(15)
        boxlayout_button_separator.add_widget(separator_image)



        # self.track_source = audio_engine.create_track(sound.samples, 120)
        self.step_buttons = []
        self.nb_steps = nb_steps
        for i in range(0, nb_steps):  # ajout des stepbutton
            step_button = TrackStepButton()  # je definis le bouton
            # if i % 8 < 4:  # V1
            if int(i/4) % 2 == 0:
                step_button.background_normal = "images/step_normal1.png"  # optionnel deja defini dans kv
            else:
                step_button.background_normal = "images/step_normal2.png"
            step_button.bind(state=self.on_step_button_state)  # je bind = affecte l'etat du bouton à une fonction
            self.step_buttons.append(step_button)
            self.add_widget(step_button)

    def on_sound_button_press(self):
        self.audio_engine.play_sound(self.sound.samples)

    def on_step_button_state(self, widget, value):  # ! lorsqu'on bind recup self,widget,value ou autre selon aide kivy
        steps = []
        for i in range(0, self.nb_steps):
            if self.step_buttons[i].state == "down":
                steps.append(1)
            else:
                steps.append(0)
        # par track on aura un track_source
        self.track_source.set_steps(steps)

