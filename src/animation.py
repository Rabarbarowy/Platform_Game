from src.sprite import Sprite


class AnimateSprite(Sprite):
    def __init__(self):
        self.width_index = 0
        self.height_index = 0
        self.animation_speed = 6
        self.animation_speed_index = 0

    def cut_part_of_image(self, image, x_frame_pos: int, y_frame_pos: int, frame_width: int, frame_height: int):
        cropped_image = image.subsurface((x_frame_pos, y_frame_pos, frame_width, frame_height))
        return cropped_image

    def animation(self, image, frame_sizes):
        image_width = image.get_width()
        image_height = image.get_height()

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
        frame = self.cut_part_of_image(image, self.width_index, self.height_index, frame_sizes[0], frame_sizes[1])

        return frame
