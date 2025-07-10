import matplotlib.pyplot as plt
import seaborn as sns

df['created'] = pd.to_datetime(df['created'])

monthly_sentiment_compound = df.resample('M', on='created')["sentiment_compound"].mean().reset_index()
monthly_sentiment_compound['created'] = pd.to_datetime(monthly_sentiment_compound['created'])
monthly_sentiment_compound = monthly_sentiment_compound[~monthly_sentiment_compound['created'].dt.year.between(2008, 2015)]

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sentiment_compound, x='created', y='sentiment_compound', marker="o")
plt.title("Average Sentiment Over Time")
plt.xlabel("Date")
plt.ylabel("Average Sentiment Score")
plt.grid(True)
plt.tight_layout()
plt.show()
