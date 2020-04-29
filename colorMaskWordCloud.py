#Importing Libraries
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import urllib
import requests
import numpy as np
import matplotlib.pyplot as plt
import wikipedia 

#Request user input
search = input('Search somthing on Wikipedia: ')

#Wikipedia search
def get_wiki(search):
    title = wikipedia.search(search)[0]
    page = wikipedia.page(title)
    return page.content

#Function data to varible
data = get_wiki(search)

#Batman mask
batman_mask = np.array(Image.open(requests.get('https://www.freepnglogos.com/uploads/yellow-black-batman-logo-png-2.png', stream=True).raw))

#Spongebob mask
spongebob_mask = np.array(Image.open(requests.get('https://pngimg.com/uploads/spongebob/spongebob_PNG11.png', stream=True).raw))

#Marvel mask
marvel_mask = np.array(Image.open(requests.get('https://logos-download.com/wp-content/uploads/2018/07/Marvel_logo_red.png', stream=True).raw))

#Simpsons mask
simpsons_mask = np.array(Image.open(requests.get('https://pngimg.com/uploads/simpsons/simpsons_PNG63.png', stream=True).raw))

#Word cloud format
word_cloud = WordCloud(width = 300, height = 300, background_color='white', stopwords=STOPWORDS, mask=simpsons_mask).generate(data)

#Creating coloring from image
image_colors = ImageColorGenerator(simpsons_mask)
plt.figure(figsize=[7,7])
plt.imshow(word_cloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
_=plt.show()
  
#Generating wordcloud
generate_wordcloud(data, simpsons_mask)