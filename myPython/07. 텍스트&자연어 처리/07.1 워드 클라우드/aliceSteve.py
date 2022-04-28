from PIL import Image   # PIL : Python Image Library
image_file = 'alice.png'
img_file = Image.open(image_file)
print(type(img_file))
print('-' * 30)

import numpy as np

alice_mask = np.array(img_file)
# print(alice_mask)
# print('-' * 30)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 8))
plt.imshow(alice_mask, interpolation='bilinear')
plt.axis('off')
filename = 'graph01.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
####################################################################################################
from wordcloud import WordCloud, STOPWORDS  # stopwords(불용어): 빈도수는 많지만 분석에서 불필요한 요소들(절대적이지 않은 단어들)

mystopwords = set(STOPWORDS)
mystopwords.add('said')
mystopwords.update(['ho', 'ha'])
# print(mystopwords)

wc = WordCloud(background_color='white', max_words=2000, stopwords=mystopwords, mask=alice_mask)
stevefile = 'steve.txt'
text = open(stevefile, 'rt', encoding='UTF-8')
text = text.read()

wc = wc.generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
filename = 'graph02.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
####################################################################################################
alice_color_file = 'alice_color.png'
alice_color_mask = np.array(Image.open(alice_color_file))

wc = WordCloud(background_color='white', max_words=2000, stopwords=mystopwords,
               mask=alice_color_mask, max_font_size=40, random_state=42)

wc = wc.generate(text)

plt.figure(figsize=(12, 12))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
filename = 'graph03.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
####################################################################################################

plt.figure(figsize=(12, 12))
plt.imshow(alice_color_mask, interpolation='bilinear')
plt.axis('off')
filename = 'graph04.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
####################################################################################################
from wordcloud import ImageColorGenerator
image_colors = ImageColorGenerator(alice_color_mask)
newwc = wc.recolor(color_func=image_colors)

plt.figure(figsize=(12, 12))
plt.imshow(newwc, interpolation='bilinear')
plt.axis('off')
filename = 'graph05.png'
plt.savefig(filename)
print(filename + ' 저장 완료')
