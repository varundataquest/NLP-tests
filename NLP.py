#Natural Language processing (NLP) tests in English

# Required and setup
# Python 3.10 or greater
# pip2 install nltk
# /Applications/Python\ 3.10/Install\ Certificates.command
# python3 -m nltk.downloader all

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string


def nlp_checks():
    text = "Chola  kings  calling  themselves  merely   by  the   title  of Rajakesarivanmn. These inscriptions have been arranged in the order of the regnal  years" \
           "  quoted in each inscription,  irrespective  of the  identity  o f the  kings  who  issued  them.   The  undated epigraphs and those  of which the date portions are damaged " \
           " or no  longer  legible have been relegated  to  the  end.   In his introductory remarks, prefixed  to  the  text  of each record,  as  well  as  in  his  general  Introduction  to  the  volume, " \
           " the  editor has  tried  to assign them to particular kings of the dynasty, giving reasons for doing so.   It is hoped that  the  volume will  be found useful  to  students of South-Indian  History," \
           "  Epigraphy and  Tamil language"

    print("NLP Basic ...................")

    # Tokenize to Sentences
    sentences = tokenize_sentence(text)
    print(len(sentences), 'sentences:', sentences)

    # Tokenize to words
    words = tokenize_word(text)
    print(len(words), 'words:', words)

    # Remove Stop words
    stop_words = get_stopwords('english')

    words = [word for word in words if word not in stop_words]
    print(len(words), "without stopwords:", words)

    # Remove Punctuations
    punctuations = get_punctuations('english')
    words = [word for word in words if word not in punctuations]
    print(len(words), "words without stopwords and punctuations:", words)


def nlp_checks_advanced():
    text = download_text()
    from nltk.tokenize import word_tokenize

    print("NLP Advanced ...................")

    #Tokenize to words
    words = tokenize_word(text)
    print(len(words), "tokens")

    #Remove stopwords
    stop_words = get_stopwords('english')
    words = [word for word in words if word not in stop_words]
    print(len(words), "tokens after stop word removal")

    #punctuations, add extra puncations to list and remove them all
    punctuations = get_punctuations('english')
    punctuations.append('”')
    punctuations.append('’')
    punctuations.append('“')
    words = [word for word in words if word not in punctuations]
    print(len(words), "tokens after stop word and punctuation removal")
    print("Without punctuations:", words)

    #Bigrams
    print("Bigrams - Top 10:", get_bigrams(words))

    #Trigrams
    print("Trigrams - Top 10:", get_trigrams(words))

    #POS Parts of Speech
    pos_tagged_text = get_pos(words)
    for pos_tag_word in pos_tagged_text:
        #print(pos_tag_word[0], ":")
        #nltk.help.upenn_tagset(pos_tag_word[1]) //this is printing a lot
        dummy=0

    #Stemmer
    for word in words:
        print("Stem of", word, get_stemmed(word))

    # Lemmatize
    for word in words:
        print("Lemmatization of", word, get_lemmatized(word))


def download_text():
    import urllib.request
    url = "http://www.gutenberg.org/files/1342/1342-0.txt"
    text = urllib.request.urlopen(url).read().decode()
    return text


def tokenize_sentence(text):
    sentences = sent_tokenize(text)
    return sentences


def tokenize_word(text):
    words = word_tokenize(text)
    return words


def get_stopwords(language):
    stop_words = stopwords.words(language)
    return stop_words


def get_punctuations(language):
    if language == 'english':
        punctuations = list(string.punctuation)
    return punctuations


def get_bigrams(words):
    from nltk.metrics import BigramAssocMeasures
    from nltk.collocations import BigramCollocationFinder
    bigram_collocation = BigramCollocationFinder.from_words(words)
    # Top 10 most occurring collocations
    return bigram_collocation.nbest(BigramAssocMeasures.likelihood_ratio, 10)


def get_trigrams(words):
    from nltk.collocations import TrigramCollocationFinder
    from nltk.metrics import TrigramAssocMeasures
    trigram_collocation = TrigramCollocationFinder.from_words(words)
    # Top 10 most occurring collocations
    return trigram_collocation.nbest(TrigramAssocMeasures.likelihood_ratio, 10)


def get_pos(words):
    pos_tagged_text = nltk.pos_tag(words)
    return pos_tagged_text


def get_stemmed(word):
    stemmer = nltk.stem.PorterStemmer()
    return stemmer.stem(word)

def get_lemmatized(word):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return lemmatizer.lemmatize(word)

if __name__ == '__main__':
    nlp_checks()
    #nlp_checks_advanced()
