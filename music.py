import pygame
import clock

class Track:
    def __init__(self, file, bpm, time_signature):

        # PARAMETERS
        self.bpm = bpm
        self.bps = bpm/60
        self.bpms = bpm/60000
        self.time_signature = time_signature
        
        # INIT
        self.clock = clock.Clock()
        self.first_beat_trigger = True
        self.current_beat = 0
        self.current_beat_in_bar = 0
        self.delta_beat = 0

        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
    
    def tick(self):
        '''
        Executed every frame.
        '''

        # Updates clock (current_time and delta_time)
        self.clock.tick()

        # Updates beat
        self.last_beat = self.current_beat
        self.current_beat = self.clock.get_elapsed_time() * self.bps
        self.current_beat_in_bar = self.current_beat % self.time_signature

    def is_on_beat(self, forgiveness):
        
        if self.current_beat_in_bar%1 < forgiveness or self.current_beat_in_bar%1 > 1-forgiveness:
            return True
        else:
            return False
        
    def is_frame_on_beat(self):
        # If first frame in beat
        if self.is_on_beat(0.1):
            if self.first_beat_trigger == True:
                self.first_beat_trigger = False
                return True
            else:
                return False
        else:
            self.first_beat_trigger = True
            return False
    
    def get_delta_beat(self):
        return self.clock.get_delta_time()