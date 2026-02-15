import arcade

from шар import Ball
from палки import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong - Два игрока"
PADDLE_WIDTH = 10
PADDLE_SPEED = 3
WHITE = (255, 255, 255)

class PongGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(WHITE)
        self.left_paddle = None
        self.right_paddle = None
        self.ball = None
        self.game_over = False
        self.winner = None  # "left" или "right"
        self.setup()

    def setup(self):
        self.left_paddle = Paddle(PADDLE_WIDTH // 2 + 20, SCREEN_HEIGHT // 2)
        self.right_paddle = Paddle(SCREEN_WIDTH - PADDLE_WIDTH // 2 - 20, SCREEN_HEIGHT // 2)
        self.ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.game_over = False
        self.winner = None

    def on_draw(self):
        self.clear()
        self.left_paddle.draw()
        self.right_paddle.draw()
        self.ball.draw()

        if self.game_over and self.winner:
            winner_text = f"Проиграла {self.winner} сторона"
            arcade.draw_text(winner_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
                             arcade.color.BLACK, font_size=24, anchor_x="center")
            arcade.draw_text("Сыграть ещё?",
                             SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20,
                             arcade.color.BLACK, font_size=20, anchor_x="center")
            arcade.draw_text("Нажмите на экран",
                             SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50,
                             arcade.color.BLACK, font_size=16, anchor_x="center")

    def on_update(self, delta_time):
        if self.game_over:
            return

        self.left_paddle.move()
        self.right_paddle.move()
        self.ball.move()
        self.ball.check_collision_with_walls()
        self.ball.check_collision_with_paddle(self.left_paddle)
        self.ball.check_collision_with_paddle(self.right_paddle)
        out_side = self.ball.is_out_of_bounds()

        if out_side:
            self.game_over = True
            self.winner = out_side

    def on_key_press(self, key, modifiers):
        if self.game_over:
            return
        if key == arcade.key.W:
            self.left_paddle.change_y = PADDLE_SPEED
        elif key == arcade.key.S:
            self.left_paddle.change_y = -PADDLE_SPEED
        elif key == arcade.key.UP:
            self.right_paddle.change_y = PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.right_paddle.change_y = -PADDLE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.left_paddle.change_y = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.right_paddle.change_y = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_over:
            self.setup()