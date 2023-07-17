class Physic:
    def __init__(self) -> None:
        self.graphitization_power = 1
        self.in_air = True

    def graphitization(self, y: int) -> int:
        y += self.graphitization_power
        self.graphitization_power += 0.5
        return y

    def resset_graphitization_power(self):
        self.graphitization_power = 0

    def collision(self, collid_object: object, second_object: object, previous_x: int, previous_y: int) -> None:
        if collid_object.x + collid_object.width >= second_object.x:
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.x = previous_x
        if collid_object.x <= second_object.x + second_object.width:
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.x = previous_x
        if collid_object.y + collid_object.height >= second_object.y:
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.y = previous_y
                self.resset_graphitization_power()
                self.in_air = False
            else:
                self.in_air = True
        if collid_object.y <= second_object.y + second_object.height:
            if collid_object.hitbox.colliderect(second_object.hitbox):
                collid_object.y = previous_y




