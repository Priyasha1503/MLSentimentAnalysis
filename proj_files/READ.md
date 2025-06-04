# 🧠 Real-Time Sentiment Analyzer

This is a simple yet powerful Sentiment Analysis app built using **Python** and **Streamlit**. It takes user input and analyzes the emotional tone of the text — identifying whether it's **Positive 😊**, **Negative 😞**, or **Neutral 😐** — using the **VADER sentiment analysis model** from the `vaderSentiment` library.

---
####Author by Priyasha Sabbavarapu

## 🔧 Tech Stack

- **Language:** Python 3
- **Libraries:**
  - [Streamlit](https://streamlit.io/) – for creating the interactive web app
  - [VADER Sentiment Analyzer](https://github.com/cjhutto/vaderSentiment) – for pre-trained rule-based sentiment scoring

---

## 🚀 How to Run

1. Clone the repo or download the files:
    ```bash
    git clone https://github.com/your-username/sentiment-analyzer.git
    cd sentiment-analyzer
    ```

2. (Optional but recommended) Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate    # or .\venv\Scripts\activate on Windows
    ```

3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:
    ```bash
    streamlit run app.py
    ```

---

## 💡 Features

- Easy-to-use web interface
- Real-time sentiment analysis with confidence scores
- Emoji feedback for fun emotional feedback 🤩
- Handles both casual and formal text input

---

## 📸 Screenshot

*(Add a screenshot of your app running here if required)*

---

## 📚 Use Cases

- Social media sentiment detection
- Product review feedback
- Mental health check-in tools
- Chatbots & smart replies

---

## 👩‍💻 Author

Built with ❤️ by [Your Name Here]

---

## 🏁 Bonus Ideas

If you want to expand the app in future:
- Add support for batch sentiment via CSV upload
- Show a pie chart of sentiment results
- Store results in a database or Google Sheets


#######################################################################
######################################################################
## 🧠 What is Sentiment Analysis?

**Sentiment Analysis** (also known as opinion mining) is a natural language processing (NLP) technique used to determine whether a piece of text expresses a **positive**, **negative**, or **neutral** sentiment.

It’s commonly used to analyze:
- Customer feedback
- Product reviews
- Social media posts
- Survey responses
- Public opinion on events or topics

This project uses the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** model, which is a pre-trained, lexicon-based sentiment analysis tool designed especially for social media and short texts. VADER can detect sentiment with reasonable accuracy and even understands emojis, slang, and capitalization!

### ✅ Example Inputs & Outputs:

| Input Text                              | Sentiment |
|-----------------------------------------|-----------|
| "I absolutely love this app!"           | Positive 😊 |
| "This is the worst experience ever."    | Negative 😞 |
| "It’s okay, not great but not terrible."| Neutral 😐 |

The model works by assigning a **compound score** between -1 (most negative) and +1 (most positive), with thresholding to categorize sentiment.


