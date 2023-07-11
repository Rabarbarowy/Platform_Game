class Physic:
    def __init__(self) -> None:
        self.graphitization_power = 1
        self.in_air = True

    def graphitization(self, y: int) -> int:
        if self.in_air:
            y += self.graphitization_power
            self.graphitization_power += 0.5
        else:
            self.graphitization_power = 0
        return y

    def collision(self, collid_object: object, second_object: object, previous_x: int, previous_y: int) -> None:
        if collid_object.hitbox.colliderect(second_object.hitbox):
            collid_object.y = previous_y
            self.in_air = False



