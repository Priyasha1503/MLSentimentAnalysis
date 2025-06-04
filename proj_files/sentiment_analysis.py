import nltk
import string
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Download NLTK data (only once needed)
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
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Clean the sentences
cleaned_sentences = [clean_text(sentence) for sentence in sentences]

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

print("\nSentiment Analysis Results:\n")

for original, cleaned in zip(sentences, cleaned_sentences):
    scores = analyzer.polarity_scores(cleaned)
    sentiment = "Neutral"
    if scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif scores['compound'] <= -0.05:
        sentiment = "Negative"
    
    print(f"Original: {original}")
    print(f"Cleaned: {cleaned}")
    print(f"Scores: {scores}")
    print(f"Sentiment: {sentiment}\n")
