import wave
from array import array


class Sound:
    samples = None
    nb_frames_samples = 0

    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(self.filename, mode="rb")
        self.nb_frames_samples = wav_file.getnframes()
        frames = wav_file.readframes(self.nb_frames_samples)  # bytes : 8bits
        self.samples = array("h", frames)  # conversion en 16 bits # self permet de stocker info au niveau de la class

    def play_sound(self):
        pass


class SoundKit:
    sounds = ()

    def get_nb_tracks(self):
        return len(self.sounds)

class SoundKit1(SoundKit):
    sounds = (Sound("./sounds/kit1/kick.wav", "KICK"),
              Sound("./sounds/kit1/clap.wav", "CLAP"),
              Sound("./sounds/kit1/shaker.wav", "SHAKER"),
              Sound("./sounds/kit1/snare.wav", "SNARE"))


class SoundKitService:
    """selection du soundkit"""
    soundkit = SoundKit1()

    def get_nb_tracks(self):
        return self.soundkit.get_nb_tracks()

    def get_song_at(self, index):
        """joue le son selon index"""
        if index >= len(self.soundkit.sounds):
            return None
        return self.soundkit.sounds[index]
