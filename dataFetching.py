import praw
import pandas as pd
import datetime

# Your Reddit credentials here
reddit = praw.Reddit(
    client_id="####################",
    client_secret="########################",
    user_agent="##########################"
)

subreddits = [
    "ImpulseBuy", "shoppingaddiction", "frugal", "BuyItForLife", "personalfinance",
    "TiktokMadeMeBuyIt", "retailhell", "Scams", "productreviews", "Anticonsumption",
    "minimalism", "povertyfinance", "debtfree", "financialindependence", "budget",
    "personalfinanceindia", "simpleliving", "NoStupidQuestions", "LifeProTips",
    "AskReddit", "TrueOffMyChest", "confession", "Vent", "CasualConversation",
    "CreditCards", "poverty", "moneydiariesactive", "Adulting", "MillennialMoney",
    "WorkReform", "antiMLM", "socialmedia", "influencermarketing", "EtsySellers"
]

queries = [
    "impulse buy", "shopping addiction", "retail therapy", "TikTok made me buy",
    "regret purchase", "bought it on a whim", "couldn’t resist",
    "unplanned purchase", "late night shopping", "Amazon haul", "online shopping spree",
    "shopping regret", "bought it for no reason", "couldn’t help myself",
    "influenced by Instagram", "influenced by TikTok", "influencer made me buy it",
    "shopping guilt", "buying things I don't need", "retail therapy session",
    "emotional spending", "addicted to shopping", "shopping binge",
    "credit card maxed out", "buy now pay later", "overspending", "consumerism trap"
]

# Collect posts
posts = []
for sub in subreddits:
    for query in queries:
        print(f"Searching r/{sub} for '{query}'...")
        try:
          for submission in reddit.subreddit(sub).search(query, limit=2000):
              if not submission.stickied:
                  posts.append({
                      "id": submission.id,
                      "title": submission.title,
                      "text": submission.selftext,
                      "subreddit": sub,
                      "score": submission.score,
                      "created": datetime.datetime.utcfromtimestamp(submission.created_utc),
                      "url": submission.url,
                      "query": query
                  })
        except:
            print(f"Error collecting posts from r/{sub}")

# Save
df = pd.DataFrame(posts).drop_duplicates(subset="id")
df.to_csv("multi_subreddit_query_reddit_data_original.csv", index=False)
print(f"✅ Saved {len(df)} posts to CSV")
