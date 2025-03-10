from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_tag = soup.find_all(name="span", class_="titleline")
article_anchors = [article.find(name="a") for article in article_tag]
article_texts = []
article_links = []

for items in article_anchors:
    text = items.getText()
    article_texts.append(text)
    link = items.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])


# --------------------------------- BASICS -------------------------------- #
    # import lxml
# with open("./website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchors = soup.find_all(name="a")
# # print(all_anchors)
#
# # for tag in all_anchors:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)
