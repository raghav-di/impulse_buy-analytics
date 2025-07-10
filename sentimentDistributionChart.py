import matplotlib.pyplot as plt

pos = 0
neu = 0
neg = 0
for s in df['sentiment_label']:
    if s == "positive":
        pos += 1
    elif s == "neutral":
        neu += 1
    elif s == "negative":
        neg += 1

labels = [ 'Negative', 'Neutral','Positive']
sizes = [neg,neu,pos]
explode = (0.1, 0, 0)
plt.pie(sizes,labels=labels,autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.show()
