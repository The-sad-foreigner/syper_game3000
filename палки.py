import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 3
GREEN = (0, 255, 0)


class Paddle:
    def __init__(self, x, y, color=GREEN):
        self.x = x
        self.y = y
        self.change_y = 0
        self.color = color
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT

    def move(self):
        self.y += self.change_y

        if self.y < self.height // 2:
            self.y = self.height // 2
        if self.y > SCREEN_HEIGHT - self.height // 2:
            self.y = SCREEN_HEIGHT - self.height // 2

    def draw(self):
        arcade.draw_lbwh_rectangle_filled(self.x, self.y - 50, self.width, self.height, self.color)