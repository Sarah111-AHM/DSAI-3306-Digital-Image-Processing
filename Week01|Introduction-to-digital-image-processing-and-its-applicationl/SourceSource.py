## to install library: pip install pillow
from PIL import Image
import numpy as np

tree_gray = Image.open("/m/Camera_team/01_team_members/mohamed/DIP/trees_gray.jpeg")
tree_gray_data = np.array(tree_gray)
print(' gray image size : ', tree_gray_data.shape)   #  gray image size :  (177, 187)
tree_gray.show()

# process the image
tree_gray_data[100,110] = 0
tree_gray_data[0:-1, 5:6] = 0

# create an image from numpy array
tree_copy = Image.fromarray(tree_gray_data)
tree_copy.show()

im = Image.open("/m/Camera_team/01_team_members/mohamed/DIP/colors.jpeg")
# copy image data into numpy array access image pixels
data = np.asarray(im)
print(data.shape) # (183, 195, 3)
im.show()

r = data[:,:,0] # red channel
g = data[:,:,1] # green channel
b = data[:,:,2] # blue channel

new_image_r = Image.fromarray(r)
new_image_r.show()

new_image_g = Image.fromarray(g)
new_image_g.show()

new_image_b = Image.fromarray(b)
new_image_b.show()
