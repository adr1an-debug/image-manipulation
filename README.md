## Image Manipulation Script

## Overview

This Python script performs several random manipulations on an image, including resizing, adding noise, cropping, rotating, flipping, and removing metadata. It can be used to create variations of an image for testing purposes, anonymize image metadata, or simply modify an image randomly.  
You can use it to add similar content on platforms like Instagram, Reddit, TikTok, etc.

## Features

- Random Resizing: Adjusts the size of the image by a random factor.
- Noise Addition: Introduces random noise to alter the pixel values of the image.
- Random Cropping: Crops a randomly selected portion of the image.
- Random Rotation: Rotates the image by a random angle within a specified range.
- Random Flipping: Flips the image horizontally with a 50% probability.
- Metadata Removal: Removes all EXIF metadata from the image to ensure privacy.

## Requirements

- Python 3.x
- Required Python libraries:
- `Pillow`
- `NumPy`

Install dependencies using pip:
```pip install pillow numpy```

## Usage

1. Set Image Paths: Update the following paths in the script:

`image_path`: The path to the input image.
`output_path`: The path where the transformed image will be saved.

2.Run the Script: After setting the paths, run the script to apply the manipulations.
```python image-manipulation.py```

3. Example of Script Use:

```
import numpy as np
from PIL import Image, ImageOps, ImageFilter
import random
import os

# Load the image
image_path = r'C:\path_to_your_image\input_image.png'
image = Image.open(image_path)

# Random transformations
image = random_resize(image)
image = add_noise(image)
image = random_crop(image)
image = random_rotate(image)
image = random_flip(image)

# Remove metadata and save the image
data = list(image.getdata())
image_without_metadata = Image.new(image.mode, image.size)
image_without_metadata.putdata(data)
output_path = r'C:\path_to_your_image\output_image.png'
image_without_metadata.save(output_path)
```

## Notes

- Ensure the input image is accessible at the specified `image_path`.
- The script applies all transformations in sequence, and the output image is saved to the `output_path`.
- You can adjust the range and intensity of each transformation by changing the parameters in the function definitions.

## License

This project is licensed under the MIT License. You are free to modify, distribute, and use it as you see fit.
