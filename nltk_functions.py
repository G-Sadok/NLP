import pandas as pd
from glob import glob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from matplotlib import pyplot as plt
from wordcloud import WordCloud


# #Function to filter correctly with lemmatize

# Stopwords

def fetch_stopwords():
    filepath="My_stopwords.txt"
    all_stopwords = set(stopwords.words('english'))
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_data = f.read()
        data = raw_data.split(",")
        my_stopwords = [word.strip().strip('"').strip("'").lower() for word in data if word.strip()]
        all_stopwords.update(my_stopwords)
        return all_stopwords
    except FileNotFoundError:
        print(f"Le fichier est introuvable")
        return []
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return []


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


#Function to clean each book text
def preprocessing(book_path):

    with open(book_path, "r") as f:
        all_text = f.read().split('End of the Project')
        
    book_without_end = all_text[0]
    # book_without_start = book_without_end.split('START OF THIS PROJECT GUTENBERG EBOOK')[1]

    book_text = book_without_end.split('\n')

    book_text = list(filter(None, book_text))
    book_word = []
    for i in book_text :
        temp_word = word_tokenize(i)
        for j in temp_word:
            book_word.append(j)
        temp_word = []

    #Redifine stopwords
    my_stopwords = fetch_stopwords()
    # nltk_stopwords = set(stopwords.words('english'))
    # indesirables = nltk_stopwords.union(my_stopwords)
    # indesirables.update(['work', 'project', 'ebook', 'gutenberg', 'Gutenberg', 'http'])

    #Removing punctuation using isalpha instead of string.punctuation
    clean_punctuation = [word for word in book_word if word.isalpha()]
    clean_book_word = [word.lower() for word in clean_punctuation if not word.lower() in my_stopwords]

    #Importing "WordNetLemmatizer" from nltk.stem to do the lemmatization
    lemmatizer = WordNetLemmatizer()

    book_lemmatized = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in clean_book_word if len(word)>1]
    return book_lemmatized

# Function to get frequencies
def book_freq(cleaned_data):
   return nltk.FreqDist(cleaned_data)


#function to generate the word cloud
def books_cloud(frequency, book_name):
    #Importing WordCloud from wordcloud to create the words cloud
    book_cloud = WordCloud(background_color="white", width=1000, height=500, colormap='rainbow', ).generate_from_frequencies(frequency)
    plt.figure(figsize = (12, 12))
    plt.imshow(book_cloud)
    plt.title(book_name)
    plt.axis("off")
    plt.show()

#function to create the bag of word
def book_freq_data(frequence):
    # book_df = pd.DataFrame.from_dict(frequence, orient='index', columns=['Frequency'])
    book_df = pd.DataFrame(frequence.items(), columns=['word', 'frequency'])
    # book_df.index.name = 'Word'
    book_df = book_df.sort_values(by='frequency', ascending=False)
    return book_df
