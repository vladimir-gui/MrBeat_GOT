from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton


class TrackStepButton(ToggleButton):
    pass


class TrackSoundButton(Button):
    pass


class TrackWidget(BoxLayout):
    """ structure d'un track """
    def __init__(self, sound, audio_engine, nb_steps, **kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        sound_button = TrackSoundButton()
        sound_button.text = sound.displayname
        sound_button.on_press = self.on_sound_button_press
        self.add_widget(sound_button)  # ajout nom du soundkit
        self.audio_engine = audio_engine
        self.sound = sound
        # self.track_source = audio_engine.create_track(sound.samples, 120)

        self.step_buttons = []
        self.nb_steps = nb_steps
        for i in range(0, nb_steps):  # ajout des stepbutton
            step_button = TrackStepButton()  # je definis le bouton
            step_button.bind(state=self.on_step_button_state)  # je bind = affecte l'etat du bouton à une fonction
            self.step_buttons.append(step_button)
            self.add_widget(step_button)

    def on_sound_button_press(self):
        self.audio_engine.play_sound(self.sound.samples)
        print("sound !")

    def on_step_button_state(self, widget, value):  # ! lorsqu'on bind recup self,widget,value ou autre selon aide kivy
        steps = []
        for i in range(0, self.nb_steps):
            if self.step_buttons[i].state == "down":
                steps.append(1)
            else:
                steps.append(0)
        print(steps)
        # par track on aura un track_source
        # self.track_source.set_steps(steps)


#     si clic sur bouton step button on realise un fonction qui genere un un tableau (tuple)
