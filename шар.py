import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
BALL_SPEED_X = 2
BALL_SPEED_Y = 2
BLACK = (0, 0, 0)

class Ball:
    def __init__(self, x, y, color=BLACK):
        self.x = x
        self.y = y
        self.change_x = 0
        self.change_y = 0
        self.color = color
        self.radius = BALL_RADIUS
        self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.change_x = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
        self.change_y = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def check_collision_with_paddle(self, paddle):
        if (self.x - self.radius <= paddle.x + paddle.width // 2 and
            self.x + self.radius >= paddle.x - paddle.width // 2):
            if (self.y - self.radius <= paddle.y + paddle.height // 2 and
                self.y + self.radius >= paddle.y - paddle.height // 2):
                self.change_x *= -1
                relative_intersect_y = (paddle.y - self.y) / (paddle.height // 2)
                self.change_y = -relative_intersect_y * BALL_SPEED_Y * 1.5
                return True
        return False

    def check_collision_with_walls(self):
        if self.y - self.radius <= 0 or self.y + self.radius >= SCREEN_HEIGHT:
            self.change_y *= -1
            return True
        return False

    def is_out_of_bounds(self):
        if self.x - self.radius <= 0:
            return "left"
        elif self.x + self.radius >= SCREEN_WIDTH:
            return "right"
        return None