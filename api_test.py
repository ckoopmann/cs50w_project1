import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "5eOT5bKjx84fcqynncVpg", "isbns": "9781632168146"})
print(res.json())
