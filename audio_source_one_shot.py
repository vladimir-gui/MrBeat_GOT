from array import array
from audiostream.sources.thread import ThreadSource


class AudioSourceOneShot(ThreadSource):
    def __init__(self, output_stream, wav_samples, *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs)
        self.chunk_nb_samples = 32
        self.wav_samples = wav_samples
        self.nb_wav_samples = len(wav_samples)
        self.current_sample_index = 0
        self.buf = array("h", b"\x00\x00" * self.chunk_nb_samples)  # \x00 equivaut à 0

    def get_bytes(self, *args, **kwargs):
        for i in range(0, self.chunk_nb_samples):
            if self.current_sample_index < self.nb_wav_samples:
                self.buf[i] = self.wav_samples[self.current_sample_index]  # buffer temporaire du chunk
            else:
                self.buf[i] = 0
            self.current_sample_index += 1

        return self.buf.tostring()
