#Importing Libraries
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt
import wikipedia 

#Request user input
search = input('Search something on Wikipedia: ')

#Wikipedia search
def get_wiki(search):
    title = wikipedia.search(search)[0]
    page = wikipedia.page(title)
    return page.content

#Function data to varible
data = get_wiki(search)

#Sample mask links
#Marvel mask: https://logos-download.com/wp-content/uploads/2018/07/Marvel_logo_red.png
#Mickey mask: https://i.pinimg.com/originals/22/92/c8/2292c8f0bf0c2e166c3c08e6adf2f014.png
#Penny mask: https://cdn.getstickerpack.com/storage/uploads/sticker-pack/penny-wise/sticker_7.png?71e44a420b56adf1f8e34b49b2374bf0
#Puppy mask: https://pngimg.com/uploads/dog/dog_PNG50375.png
#Pikachu mask: https://www.pngmart.com/files/2/Pikachu-PNG-Transparent-Image.png

#Change mask 
change_mask = 'https://logos-download.com/wp-content/uploads/2018/07/Marvel_logo_red.png'
offical_mask = np.array(Image.open(requests.get(change_mask, stream=True).raw))

#Background color
back_color = '#ffffff'

#Word cloud format
word_cloud = WordCloud(width = 300, height = 300, background_color=back_color, stopwords=STOPWORDS, mask=offical_mask).generate(data)

#Creating coloring from image
image_colors = ImageColorGenerator(offical_mask)
plt.figure(figsize=[7,7])
plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
_=plt.show()
  
