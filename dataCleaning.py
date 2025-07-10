import re

df["full_text"] = df["title"].fillna('') + " " + df["text"].fillna('')

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\d+", "", text)      # remove numbers
    text = text.lower().strip()
    return text

df["clean_text"] = df["full_text"].apply(clean_text)

analyzer = SentimentIntensityAnalyzer()

df["sentiment_score"] = df["clean_text"].apply(lambda x: analyzer.polarity_scores(x))
k = 8
df["sentiment_label"] = df["sentiment_score"].apply(
    lambda x: "positive" if (x['pos'] > x['neu']**k and x['pos'] > x['neg']) else ("negative" if (x['neg'] > x['neu']**k and x['neg'] > x['pos']) else "neutral")
)
df["sentiment_compound"] = df["sentiment_score"].apply(lambda x: x['compound'])
df["positive_score"] = df["sentiment_score"].apply(lambda x: x['pos'])
df["neutral_score"] = df["sentiment_score"].apply(lambda x: x['neu'])
df["negative_score"] = df["sentiment_score"].apply(lambda x: x['neg'])

df.to_csv("reddit_impulse_sentiment.csv", index=False)
print("✅ Sentiment added and saved.")
