import numpy as np
from PIL import Image, ImageOps
import random


image_path = r'C:\path_to_your_image\input_image.png'
image = Image.open(image_path)


def random_resize(image, max_change=0.05):
    width, height = image.size
    new_width = int(width * (1 + random.uniform(-max_change, max_change)))
    new_height = int(height * (1 + random.uniform(-max_change, max_change)))
    return image.resize((new_width, new_height))


def add_noise(image, noise_level=5):
    np_image = np.array(image)
    noise = np.random.randint(-noise_level, noise_level, np_image.shape, dtype='int16')
    np_image = np_image + noise
    np_image = np.clip(np_image, 0, 255).astype('uint8')
    return Image.fromarray(np_image)


def random_crop(image, max_change=0.05):
    width, height = image.size
    crop_width = int(width * max_change)
    crop_height = int(height * max_change)
    left = random.randint(0, crop_width)
    top = random.randint(0, crop_height)
    right = width - random.randint(0, crop_width)
    bottom = height - random.randint(0, crop_height)
    return image.crop((left, top, right, bottom))


def random_rotate(image, max_angle=5):
    angle = random.uniform(-max_angle, max_angle)
    return image.rotate(angle)


def random_flip(image):
    if random.random() < 0.5:
        return ImageOps.mirror(image)
    return image


image = random_resize(image)
image = add_noise(image)
image = random_crop(image)
image = random_rotate(image)
image = random_flip(image)


data = list(image.getdata())
image_without_metadata = Image.new(image.mode, image.size)
image_without_metadata.putdata(data)

# Saving
output_path = r'C:\path_to_your_image\output_image.png'
image_without_metadata.save(output_path)
