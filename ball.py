from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    image = None
    SPEED = 10
    RADIUS = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * self.SPEED

        canvas_width = get_canvas_width()
        if self.x < -self.RADIUS or self.x > canvas_width + self.RADIUS:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
