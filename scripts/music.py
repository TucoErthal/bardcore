import pygame

class Track:
    def __init__(self, window, file, bpm, signature):

        # PARAMETERS
        self.window = window

        # em x ms
        # tem x/1000 segundos
        # x/60000 minutos
        # x*bpm/60000 beats

        self.bpms = bpm/60000


        self.signature = signature
        
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)

        #print("FPS =", self.clock.get_fps())

    def on_beat(self, difficulty):

        self.beat_global = (pygame.mixer.music.get_pos()*self.bpms)
        self.beat_in_bar = self.beat_global%self.signature

        if self.beat_in_bar%1 < difficulty or self.beat_in_bar%1 > 1-difficulty:
            print("⬜", self.beat_in_bar)
            return True
        elif self.beat_in_bar%0.5 < difficulty or self.beat_in_bar%0.5 > 1-difficulty:
            print("🟩", self.beat_in_bar)
            return "half"
        else:
            print("🟥", self.beat_in_bar)
            return False