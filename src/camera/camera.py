class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.middle_of_x = 325
        self.middle_of_y = 200

    def update_position(self, player_x: int, player_y: int) -> None:
        if self.x > player_x - self.middle_of_x:
            self.x -= (self.x - player_x + self.middle_of_x) / 15
            # self.x = player_x - self.middle_of_x
        if self.x < player_x - self.middle_of_x:
            self.x += -(self.x - player_x + self.middle_of_x) / 15
            # self.x = player_x - self.middle_of_x

        self.y = player_y - self.middle_of_y

