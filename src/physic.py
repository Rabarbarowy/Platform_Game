class Physic:
    def __init__(self) -> None:
        self.gravitation_power = 1
        self.in_air = True
        self.collided = False
        self.y_of_object = 0

    def gravitation(self, y: int) -> int:
        if self.in_air:
            y += self.gravitation_power
            self.gravitation_power += 0.6
        return y

    def resset_gravitation_power(self) -> None:
        self.gravitation_power = 0

    def collision(self, collid_object, second_object, previous_x: int, gravitation_index, jumping: bool) -> None:
        if collid_object.hitbox.colliderect(second_object.hitbox):  # from left and right
            collid_object.x = previous_x
            self.collided = True
            self.y_of_object = second_object.y
        if collid_object.y + collid_object.height >= second_object.y and not jumping:  # from up
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.y = second_object.y - collid_object.height
                self.resset_gravitation_power()
                self.in_air = False
            else:
                if gravitation_index.hitbox.colliderect(second_object.hitbox):
                    self.resset_gravitation_power()
                    self.in_air = False
                else:
                    self.in_air = True
        elif collid_object.y <= second_object.y + second_object.height:  # from down
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.y = second_object.y + second_object.height
                self.gravitation_power = 0

