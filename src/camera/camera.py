class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def update_position(self, player_x: int, player_y: int) -> None:
        self.x = player_x - 325
        self.y = player_y - 200
