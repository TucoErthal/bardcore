import clock

class Animation():
    def __init__(self, total_frames):
        self.total_frames = total_frames
        self.current_frame = 0
        self.frame_progress = 0
        self.animation_clock = clock.Clock()
        self.sprites = [
            "assets/textures/gui/crosshair0.png",
            "assets/textures/gui/crosshair1.png",
            "assets/textures/gui/crosshair2.png",
            "assets/textures/gui/crosshair3.png",
            "assets/textures/gui/crosshair4.png",
            "assets/textures/gui/crosshair5.png",
            "assets/textures/gui/crosshair6.png",
            "assets/textures/gui/crosshair7.png",
            "assets/textures/gui/crosshair8.png",
            "assets/textures/gui/crosshair9.png",
            "assets/textures/gui/crosshair10.png",
            "assets/textures/gui/crosshair11.png",
            "assets/textures/gui/crosshair12.png",
            "assets/textures/gui/crosshair13.png",
            "assets/textures/gui/crosshair14.png",
            "assets/textures/gui/crosshair15.png"
        ]

    def set_duration(self, duration): # duration em ms
        self.frame_time = duration/self.total_frames
    
    def update(self):
        self.animation_clock.tick()
        self.frame_progress += self.animation_clock.get_delta_time()

        if self.frame_progress >= self.frame_time:
            self.frame_progress -= self.frame_time
            if self.current_frame < (self.total_frames):
                self.current_frame += 1
            else:
                self.current_frame = 0