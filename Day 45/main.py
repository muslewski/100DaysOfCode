from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titleList = soup.find_all(class_="listicleItem_listicle-item__title__BfenH")
with open("./top100.txt", "w") as file:
    for title in titleList[::-1]:
        text = title.getText()
        file.write(f"{text}\n")







# response = requests.get("https://news.ycombinator.com/news")
# soup = BeautifulSoup(response.text, "html.parser")

# article_tag = soup.select_one(".titleline a")
# article_text = article_tag.getText()
#
# article_link = article_tag.get("href")
# print(article_link)
#
# article_score = soup.find(class_="score").getText()
# print(article_score)

# scoreObjects = soup.select(".score")
# highest = 0
# highestId = ""
#
# for score in scoreObjects:
#     scoreId = score.attrs["id"]
#     score = int(score.getText().split()[0])
#     if score > highest:
#         highest = score
#         highestId = scoreId
#
# print(highest)
# print(highestId)
# #  split highest id so that we will have only numbers score_41105944
# desiredId = highestId.split('_')[1]
#
# # desiredOne = soup.find_all(id=desiredId, class_="athing")
# desiredOne = soup.find(id=desiredId, class_="athing")
# print(desiredOne.getText())