import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PSET 0: The Dot"
DOT_RADIUS = 20
DOT_SPEED = 300  # Pixels per second


class DotGame(arcade.Window):

    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # C1: Core player position
        self.x = width / 2
        self.y = height / 2

        # Movement control flags
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # C6: Moving target object state
        self.target_x = 200
        self.target_y = 400
        self.target_radius = 15
        self.target_dx = 220  # Pixels per second horizontally
        self.target_dy = 160  # Pixels per second vertically

    def on_draw(self):
        """Render frame elements."""
        self.clear()

        # C6: Draw non-controlled second object
        arcade.draw_circle_filled(
            self.target_x, self.target_y, self.target_radius, arcade.color.RED
        )

        # C1: Draw player circle
        arcade.draw_circle_filled(
            self.x, self.y, DOT_RADIUS, arcade.color.ELECTRIC_BLUE
        )

    def on_update(self, delta_time: float):
        """Update game logic using time-aware movement."""
        # Player movement
        if self.move_right:
            self.x += DOT_SPEED * delta_time
        if self.move_left:
            self.x -= DOT_SPEED * delta_time
        if self.move_up:
            self.y += DOT_SPEED * delta_time
        if self.move_down:
            self.y -= DOT_SPEED * delta_time

        # Player boundary rule (clamping inside window)
        self.x = max(DOT_RADIUS, min(self.x, SCREEN_WIDTH - DOT_RADIUS))
        self.y = max(DOT_RADIUS, min(self.y, SCREEN_HEIGHT - DOT_RADIUS))

        # Target movement
        self.target_x += self.target_dx * delta_time
        self.target_y += self.target_dy * delta_time

        # Target bouncing logic (Left/Right)
        if self.target_x - self.target_radius <= 0:
            self.target_x = self.target_radius
            self.target_dx *= -1
        elif self.target_x + self.target_radius >= SCREEN_WIDTH:
            self.target_x = SCREEN_WIDTH - self.target_radius
            self.target_dx *= -1

        # Target bouncing logic (Top/Bottom)
        if self.target_y - self.target_radius <= 0:
            self.target_y = self.target_radius
            self.target_dy *= -1
        elif self.target_y + self.target_radius >= SCREEN_HEIGHT:
            self.target_y = SCREEN_HEIGHT - self.target_radius
            self.target_dy *= -1

    def on_key_press(self, key: int, modifiers: int):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.move_left = True
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.move_right = True
        elif key in (arcade.key.UP, arcade.key.W):
            self.move_up = True
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.move_down = True

    def on_key_release(self, key: int, modifiers: int):
        if key in (arcade.key.LEFT, arcade.key.A):
            self.move_left = False
        elif key in (arcade.key.RIGHT, arcade.key.D):
            self.move_right = False
        elif key in (arcade.key.UP, arcade.key.W):
            self.move_up = False
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.move_down = False


def main():
    game = DotGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()