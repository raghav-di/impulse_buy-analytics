import pandas as pd
import matplotlib.pyplot as plt

df["created"] = pd.to_datetime(df["created"], errors="coerce")

df["year"] = df["created"].dt.year

df = df[(df["year"] >= 2016) & (df["year"] <= 2024)]

post_counts = df["year"].value_counts().sort_index()

plt.figure(figsize=(10, 5))
plt.plot(post_counts.index, post_counts.values, marker='o', linestyle='-')
plt.title("Total Number of Impulse Buying related Posts per Year")
plt.xlabel("Year")
plt.ylabel("Number of Posts")
plt.grid(True)
plt.tight_layout()
plt.show()
