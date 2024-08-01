import string
import spacy
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    # Convert to lowercase
    text = text.lower()
    
     # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Process text with spacy
    doc = nlp(text)

    # Lemmatize and remove stop words
    tokens = [token.lemma_ for token in doc if not token.is_stop]

    # Join the tokens back into a single string
    return ' '.join(tokens)

def preprocess_texts(texts):
    return [preprocess_text(text) for text in texts]

def generate_word_cloud(text, title):
    wordcloud = WordCloud(width=800, height=400).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()