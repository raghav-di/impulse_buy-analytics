import pandas as pd
import matplotlib.pyplot as plt

df["created"] = pd.to_datetime(df["created"])

df["year"] = df["created"].dt.year
df = df[(df["year"] > 2015) & (df["year"] <= 2025)]

sentiment_counts = df.groupby(["year", "sentiment_label"]).size().unstack(fill_value=0)

sentiment_percent = sentiment_counts.div(sentiment_counts.sum(axis=1), axis=0) * 100

plt.figure(figsize=(12, 6))
for sentiment in sentiment_percent.columns:
    plt.plot(sentiment_percent.index, sentiment_percent[sentiment], marker='o', label=sentiment.capitalize())

plt.title("Percentage of Sentiment Categories Over Years")
plt.xlabel("Year")
plt.ylabel("Percentage (%)")
plt.legend(title="Sentiment")
plt.grid(True)
plt.tight_layout()
plt.show()
