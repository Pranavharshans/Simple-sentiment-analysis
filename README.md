# Simple Sentiment Analysis

Minimal Streamlit web app that classifies user-provided text as Positive, Neutral, or Negative using TextBlob polarity analysis.

## Setup

```bash
python -m venv myenv
source myenv/bin/activate   # Windows: myenv\Scripts\activate
pip install streamlit==0.89.0 textblob==0.15.3
```

## Usage

```bash
streamlit run sentiment_app.py
```

Enter text in the input field and click **Analyze**. The app displays the sentiment classification with an emoji.

### Example

| Input | Output |
|-------|--------|
| "I love this product!" | Positive |
| "This is terrible." | Negative |
| "It's okay, nothing special." | Neutral |

## How It Works

The app uses TextBlob's sentiment polarity score. A configurable threshold (default 0.2) determines the classification:

- Polarity > 0.2 → Positive
- Polarity < -0.2 → Negative
- Otherwise → Neutral

## Project Structure

```
Simple-sentiment-analysis/
├── sentiment_app.py    # Streamlit application
├── requirements for running.txt
└── .gitignore
```
