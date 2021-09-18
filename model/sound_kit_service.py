

class Sound:
    def __init__(self, filename, displayname):
        self.filename = filename
        self.displayname = displayname


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
    soundkit = SoundKit()

    def get_nb_tracks(self):
        return self.soundkit.get_nb_tracks()
