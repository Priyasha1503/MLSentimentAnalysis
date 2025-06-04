import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit UI
st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠")
st.title("🧠 Real-Time Sentiment Analyzer")
st.markdown("Enter some text below and let the AI tell you if it's happy, angry, or just meh 😐")

# Input box
user_input = st.text_area("📝 Type your sentence here:")

# Analyze button
if st.button("🔍 Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Oops! Please enter some text first.")
    else:
        # Use original input directly (no cleaning)
        scores = analyzer.polarity_scores(user_input)
        compound = scores['compound']

        # Determine sentiment
        if compound >= 0.05:
            sentiment = "Positive 😊"
        elif compound <= -0.05:
            sentiment = "Negative 😞"
        else:
            sentiment = "Neutral 😐"

        # Output results
        st.subheader("🧾 Results:")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Confidence Scores:**")
        st.json(scores)
