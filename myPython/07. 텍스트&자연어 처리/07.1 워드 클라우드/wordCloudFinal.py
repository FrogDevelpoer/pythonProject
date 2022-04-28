from PIL import Image
image_file = 'alice.png'
img_file = Image.open(image_file)

import numpy as np

alice_mask = np.array(img_file)

from wordcloud import WordCloud

wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask)
backfile = 'heart-of-darkness.txt'
text = open(backfile, 'rt', encoding='UTF-8')
text = text.read()

wc = wc.generate(text)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
filename = 'wordCloudFinal.png'
plt.savefig(filename)