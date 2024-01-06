import streamlit as st
from textblob import TextBlob
from dataclasses import dataclass




@dataclass
class Mood:
    emoji: str
    sentiment: float




def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return Mood('😃 Positive', sentiment)
    elif sentiment <= hostile_threshold:
        return Mood('😠 Negative', sentiment)
    else:
        return Mood('😐 Neutral', sentiment)



def main():
    st.title("Simple Sentiment Analysis Web App")
    st.write("Enter text and click the 'Analyze' button to analyze")

    text = st.text_area("Enter your text here:")
    threshold = 0.3  



    if st.button("Analyze") and text:
        mood = get_mood(text, threshold=threshold)
        st.subheader("Sentiment Analysis Result")
        st.write(f'Sentiment: {mood.emoji} ({mood.sentiment})')



if __name__ == '__main__':
    main()
