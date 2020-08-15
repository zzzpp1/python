import requests
from PIL import Image
import matplotlib.pyplot as plt

r = requests.get('https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png')
with open('myphoto.jpg', 'wb') as f:
    f.write(r.content)

img = Image.open('myphoto.jpg')
plt.imshow(img)