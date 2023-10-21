from src.sprite import Sprite


class AnimateSprite(Sprite):
    def __init__(self):
        self.width_index = 0
        self.height_index = 0
        self.animation_speed = 6
        self.animation_speed_index = 0

    def animation(self, image, frame_sizes):
        image_width = image.get_width()
        image_height = image.get_height()
        position_of_frame = []

        if self.width_index >= image_width - frame_sizes[0]:
            if self.height_index >= image_height - frame_sizes[1]:
                self.width_index = 0
                self.height_index = 0
            else:
                self.height_index += frame_sizes[1]
                self.width_index = 0
        else:
            if self.animation_speed_index >= self.animation_speed:
                self.width_index += frame_sizes[0]
                self.animation_speed_index = 0

        self.animation_speed_index += 1

        position_of_frame.append(self.width_index)
        position_of_frame.append(self.height_index)

        return position_of_frame
