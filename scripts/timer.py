import time
from enum import Enum

class timer_state(Enum):
    RUNNING = 0, 
    PAUSED = 1,
    STOPED = 2


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = time.time()

        self.time_lapsed = 0
        self.state = timer_state.RUNNING
    
    def start(self):
        if self.state != timer_state.STOPED:
            self.restart()
            return
        
        print("use restart() to restart after you have stopped")
        
    def restart(self):
        old_time = self.get_time()

        self.state = timer_state.RUNNING
        self.start_time = time.time()
        self.end_time = self.start_time

        return old_time

    def pouse(self):
        self.state = timer_state.PAUSED

    def stop(self):
        self.state = timer_state.STOPED

    def get_time(self):
        if self.state == timer_state.RUNNING:
            self.end_time = time.time()
            self.time_lapsed = self.end_time - self.start_time

        return self.time_lapsed
    
    
