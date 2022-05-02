from PIL import Image
image_file = 'alice_color.png'
img_file = Image.open(image_file)

import numpy as np

alice_mask = np.array(img_file)

from wordcloud import WordCloud

wc = WordCloud(background_color='white', mask=alice_mask)
backfile = '애국가.txt'
text = open(backfile, 'rt', encoding='UTF-8')
text = text.read()

wc = wc.generate(text)

import matplotlib.pyplot as plt
plt.rtParams['font.family'] = 'Malgun Gothic'
plt.rtParams['axes.unicode_minus'] =False
plt.figure(figsize=(5, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
filename = 'wordCloudFinal02.png'
plt.savefig(filename)

