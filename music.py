import pygame
import clock

class Track:
    def __init__(self, file, bpm, time_signature):

        # PARAMETERS
        self.bpm = bpm
        self.bps = bpm/60
        self.bpms = self.bps/1000
        self.time_signature = time_signature

        self.latency_seconds = 0
        self.forgiveness = 0.1
        
        # INIT
        self.clock = clock.Clock()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
    
    def tick(self):
        self.clock.tick()

        self.latency_beats = self.latency_seconds * self.bps

        self.current_beat = (self.clock.get_elapsed_time() * self.bps)
        self.current_beat_in_bar = self.current_beat % self.time_signature
        self.current_beat_progress = self.current_beat % 1
        self.current_beat_progress_with_latency = self.current_beat % 1 - self.latency_beats

    def is_on_beat(self):
        if self.current_beat_progress_with_latency < self.forgiveness or self.current_beat_progress_with_latency > (1 - self.forgiveness):
            return True
        else:
            return False