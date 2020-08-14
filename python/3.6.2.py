import numpy as np
from PIL import Image
image = Image.open(r'C:\Users\zhang\Desktop\python_basic-2020-7-23-10-6-34-165-master\image.jpg')
image.show()
image_array = np.array(image)
im2 = np.sum(image_array, axis=2)
im2[...,:] = im2[...,:]/3.0
image1=Image.fromarray(im2)
image1.show()