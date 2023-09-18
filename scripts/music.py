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

        beat = pygame.mixer.music.get_pos()*self.bpms

        # Se o beat estiver entre 
        if beat%1 < difficulty or beat%1 > 1-difficulty:
            print("⬜", beat)
            return True
        else:
            print("🟥", beat)
            return False