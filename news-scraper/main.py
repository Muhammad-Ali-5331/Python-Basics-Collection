from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text,"lxml")
tags = soup.select(selector=".titleline")
anchor_texts = [first_anchor.find("a").getText() for first_anchor in tags]
anchor_link = [first_anchor.find("a").get("href") for first_anchor in tags]
anchor_upvote = [int(s.getText().split("points")[0]) for s in soup.select(selector= ".score")]
# print(anchor_texts)
# print(anchor_link)
# print(anchor_upvote)
max_vote = max(anchor_upvote)
index = anchor_upvote.index(max_vote)
print(f"Maximum Upvote: {max_vote}\nArticle Title: {anchor_texts[index]}\nArticle Link: {anchor_link[index]}")