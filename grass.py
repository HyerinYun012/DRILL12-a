from pico2d import load_image


class Grass:
    def __init__(self, dy):
        self.image = load_image('grass.png')

    def draw(self):
        global dy
        self.image.draw(400, 30, dy)

    def update(self):
        pass
