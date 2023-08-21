from src.sprite import Sprite


class AnimateSprite(Sprite):
    def __init__(self, image_of_activity, size_index: int):
        self.image = self.transform_size(image_of_activity, size_index)

    def animate_frame(self):
        return 'something'
