pip install pillow
from PIL import Image
import numpy as np

image = Image.open('/contet/your image path.jpg').convert('L')
imgarray = np.array(image)

#Bitplanes extraction
def extract_bit_planes(img_array):
    bit_planes = []
    for i in range(8):
        bit_plane = (img_array >> i) & 1
        bit_plane = (bit_plane * 255).astype(np.uint8)  # Visualization 0-255
        bit_planes.append(Image.fromarray(bit_plane))
    return bit_planes

bit_planes = extract_bit_planes(img_array)

#Saving and showing thee planes
for i, plane in enumerate(bit_planes):
    plane.save(f'bit_plane{i+1}.png')
    plane.show()
