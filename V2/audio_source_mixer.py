from array import array

from audiostream.sources.thread import ThreadSource

from audio_source_track import AudioSourceTrack

MAX_16BITS = 32767
MIN_16BITS = -32768

def sum_16bits(n):
    """fonction statique ne depend pas de la classe -- correction du probleme d'overflow"""
    s = sum(n)
    if s < MIN_16BITS:
        s = MIN_16BITS
    if s > MAX_16BITS:
        s = MAX_16BITS
    return s


class AudioSourceMixer(ThreadSource):
    buf = None

    # mixer -> starter  <<< but synchroniser les tracks
    #   get_bytes (appelé par la carte son)
    #       -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #           get_bytes (appelé à la main)   #   -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #       -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #           get_bytes (appelé à la main)   #   -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #       -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #           get_bytes (appelé à la main)   #   -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #       -> AudioSourceTrack (on les start pas) on utilise comme fonction
    #           get_bytes (appelé à la main)   #   -> AudioSourceTrack (on les start pas) on utilise comme fonction

    def __init__(self, output_stream, all_wav_samples, bpm, sample_rate, nb_steps, on_current_step_changed, min_bpm, *args, **kwargs):
        ThreadSource.__init__(self, output_stream, *args, **kwargs)

        self.tracks = []
        for i in range(0, len(all_wav_samples)):
            track = AudioSourceTrack(output_stream, all_wav_samples[i], bpm, sample_rate, min_bpm)
            track.set_steps((0,) * nb_steps)
            self.tracks.append(track)  # memorise les pas dans le track

        self.bpm = bpm
        self.buf = None
        self.silence = array("h", b"\x00\x00" * self.tracks[0].buffer_nb_samples)
        self.nb_steps = nb_steps
        self.min_bpm = min_bpm
        self.current_sample_index = 0
        self.current_step_index = 0
        self.sample_rate = sample_rate
        self.on_current_step_changed = on_current_step_changed
        self.is_playing = False

    def set_steps(self, index, steps):
        if index >= len(self.tracks):
            return

        if not len(steps) == self.nb_steps:
            self.tracks[index].set_steps(steps)

    def set_bpm(self, bpm):
        if bpm < self.min_bpm:
            return
        self.bpm = bpm

    def audio_play(self):
        self.is_playing = True

    def audio_stop(self):
        self.is_playing = False

    def get_bytes(self, *args, **kwargs):  # chemin critique = besoin de reponse temps reel ! MEF au boucles

        for i in range(0, len(self.tracks)):
            self.tracks[i].set_bpm(self.bpm)  # calage des tracks sur le bpm

        step_nb_samples = self.tracks[0].step_nb_samples

        # silence
        if not self.is_playing:
            return self.silence[0:step_nb_samples].tobytes()

        track_buffers = []
        for i in range(0, len(self.tracks)):  # + track + la boucle est longue
            track = self.tracks[i]
            track_buffer = track.get_bytes_array()
            track_buffers.append(track_buffer)

        # for i in range(0, step_nb_samples):
        #     self.buf[i] = 0
        #     for j in range(0, len(track_buffers)):
        #         self.buf[i] += track_buffers[j][i]  # addition des buffer de tous les track pour synchronisation

        s = map(sum_16bits, zip(*track_buffers))
        self.buf = array("h", s)

        # ici on envoi current_step_index à notre PlayIndicator
        if self.on_current_step_changed is not None:
            """decalage de steps pour sychroniser affichage step à l'audio (à cause buffer audio)"""
            step_index_for_display = self.current_step_index - 2  # le top serait d'ajouter dans librairie Audiostream
            if step_index_for_display < 0:
                step_index_for_display += self.nb_steps
            self.on_current_step_changed(step_index_for_display)

        self.current_step_index += 1
        if self.current_step_index >= self.nb_steps:
            self.current_step_index = 0

        return self.buf[0:step_nb_samples].tobytes()
