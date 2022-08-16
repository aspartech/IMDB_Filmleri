from bs4 import BeautifulSoup
import requests
import lxml


url = "https://www.imdb.com/chart/top"
requests = requests.get(url)

soup = BeautifulSoup(requests.content, "lxml")

print(soup)

top_250 = soup.find("tbody", attrs= {"class":"lister-list"}).find_all("tr")

sira=1

for film in top_250:
    name = film.find("tb", attrs= {"class":"titleColumn"}).a.text
    year= film.find("tb", attrs= {"class":"titleColumn"}).span.text
    puan = film.find("tb", attrs= {"class":"ratingColumn"}).stong.get("title")

    print("sira:",sira)
    print("adi:" ,name)
    print("yili:",year)
    print("puan:",puan)

    print("\n\n")

    sira += 1

