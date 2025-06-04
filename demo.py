import nltk
import string
from nltk.corpus import stopwords

# Download stopwords if you haven't yet
nltk.download('stopwords')

# Sample sentences
sentences = [
    "I love this product! It's amazing 😊",
    "This is the worst experience I've ever had.",
    "Meh, it was okay... nothing special.",
    "Absolutely fantastic! Highly recommend it.",
    "Not good, not bad, just average."
]

stop_words = set(stopwords.words('english'))

def clean_text(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

cleaned_sentences = [clean_text(sentence) for sentence in sentences]

for original, cleaned in zip(sentences, cleaned_sentences):
    print(f"Original: {original}")
    print(f"Cleaned: {cleaned}\n")
