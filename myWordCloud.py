from wordcloud import WordCloud
import wikipedia 
import matplotlib.pyplot as plt

search = input('Search somthing on Wikipedia: ')

def get_wiki(search):
    title = wikipedia.search(search)[0]
    page = wikipedia.page(title)
    return page.content

cloud = WordCloud(background_color="white").generate(get_wiki(search))

plt.imshow(cloud)
plt.axis('off')
plt.show()