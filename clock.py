import time

class Clock():
    def __init__(self):
        self.current_time = time.perf_counter()
        self.start_time = self.current_time
        self.delta_time = 0
    
    def tick(self):
        self.last_time = self.current_time
        self.current_time = time.perf_counter()

        self.delta_time += 1000*(self.current_time - self.last_time) # medido em ms

    def get_elapsed_time(self):
        return self.current_time - self.start_time

    def get_delta_time(self):
        result = self.delta_time
        self.delta_time = 0
        return result