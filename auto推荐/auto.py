import requests
from bs4 import BeautifulSoup

all_url = "https://www.juzikong.com/?type=hot"

first_html = requests.get(all_url)
# print(first_html.text)

soup = BeautifulSoup(first_html.text, "html.parser")
all_a = soup.find("div", class_="body_2l9IL").find_all("a", class_="contentLink_1ankk")
print(all_a)
