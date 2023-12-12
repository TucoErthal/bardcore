import time
from enum import Enum
from pygame import display

class timer_state(Enum):
    RUNNING = 0, 
    PAUSED = 1,
    STOPED = 2


class Timer:
    def __init__(self, max_time = -1):
        self.start_time = time.time() # The falue of the bigining
        self.last_time = time.time() # The current time
        
        self.max_time = max_time

        self.time_lapsed = 0 # start - last time
        self.state = timer_state.RUNNING 

        self.start()
    
    def start(self):
        if self.state != timer_state.STOPED:
            self.restart()
            return
        
        print("use restart() to restart after you have stopped")

    def set_max_time(self, val: int):
        self.max_time = val

    def restart(self):
        old_time = self.get_time()

        self.state = timer_state.RUNNING
        self.start_time = time.time()
        self.last_time = self.start_time

        return old_time

    def pouse(self):
        self.state = timer_state.PAUSED

    def stop(self):
        self.state = timer_state.STOPED

    def get_time(self):
        if self.state == timer_state.RUNNING:
            self.last_time = time.time()
            self.time_lapsed = self.last_time - self.start_time

        return self.time_lapsed

    def ringing(self):
        if self.get_time() > self.max_time:
            return True
        
        return False
        