from audiostream.core import get_output

from audio_source_one_shot import AudioSourceOneShot


class AudioEngine:
    NB_CHANNELS = 1
    SAMPLE_RATE = 44100
    BUFFER_SIZE = 1024

    def __init__(self):
        self.output_stream = get_output(channels=self.NB_CHANNELS, rate=self.SAMPLE_RATE, buffersize=self.BUFFER_SIZE)

    def play_sound(self, wav_samples):
        audio_source = AudioSourceOneShot(self.output_stream, wav_samples)
        audio_source.start()
