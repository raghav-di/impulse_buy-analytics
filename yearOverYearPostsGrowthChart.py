import pandas as pd
import matplotlib.pyplot as plt

df["created"] = pd.to_datetime(df["created"], errors="coerce")
df["year"] = df["created"].dt.year

df = df[df["year"] >= 2016]

yearly_post_counts = df["year"].value_counts().sort_index()

growth_rate = yearly_post_counts.diff()  

plt.figure(figsize=(10, 5))
plt.plot(growth_rate.index, growth_rate.values, marker='o', linestyle='-', color='orange')
plt.axhline(0, color='gray', linestyle='--')
plt.title("Year-over-Year Growth in Number of Reddit Posts")
plt.xlabel("Year")
plt.ylabel("Growth in Number of Posts")
plt.grid(True)
plt.tight_layout()
plt.show()
