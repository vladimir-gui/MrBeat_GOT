from array import array
from audiostream.sources.thread import ThreadSource


class AudioSourceTrack(ThreadSource):
    # nb_wav_samples = 0
    steps = ()  # mise en place des steps
    step_nb_samples = 0
    buf = None
    # bpm = 120  # 1 battement = 4 pas = 1 noire
    # # 1 battement = (44100 x 60 samples par minute) / BPM
    # # 1 pas = 1/4 batt = (44100 x 60) / (4 x BPM) = (44110 x 15) / BPM

    def __init__(self, output_stream, wav_samples, bpm, sample_rate , *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs)
        self.wav_samples = wav_samples
        self.nb_wav_samples = len(wav_samples)
        self.current_sample_index = 0
        self.current_step_index = 0
        self.bpm = bpm
        self.sample_rate = sample_rate
        self.compute_step_nb_samples_and_alloc_buffer()

    def set_steps(self, steps):
        if not len(steps) == self.steps:
            self.current_step_index = 0
        self.steps = steps

    def bpm(self, bpm):
        self.bpm = bpm
        self.compute_step_nb_samples()

    def compute_step_nb_samples_and_alloc_buffer(self):
        # step_nb_samples = (sample_rate x 15) / BPM
        if not self.bpm == 0:
            n = int(self.sample_rate*15/self.bpm)
            if not n == self.step_nb_samples:  # ne refait pas allocation buffer si identique ou inferieur
                self.step_nb_samples = n
                self.buf = array("h", b"\x00\x00" * self.step_nb_samples)

    def get_bytes(self, *args, **kwargs):

        for i in range(0, self.step_nb_samples):
            if len(self.steps) > 0:
                if self.steps[self.current_step_index] == 1:
                    # lancer mon son
                    self.buf[i] = self.wav_samples[i]  # buffer temporaire du chunk
                else:
                    self.buf[i] = 0
            else:
                self.buf[i] = 0

        self.current_sample_index += 1

        if self.current_step_index >= len(self.steps):
            self.current_step_index = 0

        return self.buf.tobytes()
