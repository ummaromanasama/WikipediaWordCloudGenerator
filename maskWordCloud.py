from wordcloud import WordCloud, STOPWORDS
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

#Batman mask for word cloud
batman_mask = np.array(Image.open(requests.get('https://cdn.onlinewebfonts.com/svg/img_509803.png', stream=True).raw))

# This function takes in your text and your mask and generates a wordcloud. 
def generate_wordcloud(data, batman_mask):
    word_cloud = WordCloud(width = 300, height = 300, background_color='white', stopwords=STOPWORDS, mask=batman_mask).generate(data)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
#Run the following to generate your wordcloud
generate_wordcloud(data, batman_mask)