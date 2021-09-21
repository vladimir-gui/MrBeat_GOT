from audiostream.core import get_output

from audio_source_one_shot import AudioSourceOneShot
from audio_source_track import AudioSourceTrack


class AudioEngine:
    NB_CHANNELS = 1
    SAMPLE_RATE = 44100
    BUFFER_SIZE = 1024

    def __init__(self):
        self.output_stream = get_output(channels=self.NB_CHANNELS, rate=self.SAMPLE_RATE, buffersize=self.BUFFER_SIZE)

        self.audio_source_one_shot = AudioSourceOneShot(self.output_stream)
        self.audio_source_one_shot.start()

    def play_sound(self, wav_samples):
        self.audio_source_one_shot.set_wave_samples(wav_samples)

    def create_track(self, wav_samples, bpm):
        source_track = AudioSourceTrack(self.output_stream, wav_samples, bpm, self.SAMPLE_RATE)
        # source_track.set_steps((1, 0, 0, 0))  # generation track manuel
        # source_track.start()
