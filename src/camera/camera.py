from src.constants import WINDOW_HEIGHT, WINDOW_WIDTH, BACKGROUND_IMAGE


class Camera:
    def __init__(self, middle_of_map) -> None:
        self.x = 0
        self.y = 0
        self.middle_of_x = WINDOW_WIDTH / 2.2
        self.middle_of_y = WINDOW_HEIGHT / 2.5
        self.middle_of_map = middle_of_map
        self.background_img = BACKGROUND_IMAGE

    def update_position(self, player_x: int, player_y: int) -> None:
        if self.x > player_x - self.middle_of_x:
            self.x -= (self.x - player_x + self.middle_of_x) / 15
            # self.x = player_x - self.middle_of_x
        if self.x < player_x - self.middle_of_x:
            self.x += -(self.x - player_x + self.middle_of_x) / 15
            # self.x = player_x - self.middle_of_x

        self.y = player_y - self.middle_of_y

