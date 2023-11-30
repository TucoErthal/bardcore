from item.init_assets import *



# HOW TO USE:
# torch_name = item.torch.Torch(args) -> initialize (do so on itemlist.py)
# torch_name.draw()                    -> draws the room and checks collisions (must be under player)


class Torch():
    def __init__(self, x, y):
        self.torch_timer = 0
        self.torch_frame = torch1
        self.x = x * 16
        self.y = y * 16

    def draw(self):
        if self.torch_timer > 0:
            self.torch_timer -= 1
        else:
            self.torch_timer = 80

        if self.torch_timer > 60:
            self.torch_frame = torch1
        elif self.torch_timer > 40:
            self.torch_frame = torch2
        elif self.torch_timer > 20:
            self.torch_frame = torch3
        else:
            self.torch_frame = torch2


        window.render(self.torch_frame, (self.x, self.y))