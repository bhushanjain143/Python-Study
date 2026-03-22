import requests
query = "tesla"#input("Enter the news title do you wan't to search")
api = "b4ccf8094e3d4fd3be7f8b270d217633"

url  = f"https://newsapi.org/v2/everything?q={query}&from=2025-12-18&sortBy=publishedAt&apiKey={api}"

print(url)

r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in items(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
