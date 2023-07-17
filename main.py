import requests
from random import choice, randint
from bs4 import BeautifulSoup

satisfied = "no"
mood = input("are you happy / sad / bored / depressed / horny / hungry : ")
while mood not in ["happy", "sad", "depressed", "bored", "horny", "hungry"]:
    mood = input("please select one of the listed keywords : ")

recommandation = {
    "happy": choice((1, 2, 10, 22, 36, 10)),
    "sad": choice((1, 2, 4, 8, 10, 30, 37)),
    "depressed": choice((1, 2, 5, 7, 24, 37, 41)),
    "bored": choice((1, 2, 10, 14, 7, 24, 37, 41)),
    "horny": choice((9, 12, 49)),
    "hungry": 47,
}

def get_recommendation_list():
    r = requests.get(f"https://myanimelist.net/anime/genre/{str(recommandation[mood])}?page={randint(1,5)}")
    if r.status_code != 200:
        r = requests.get(f"https://myanimelist.net/anime/genre/{str(recommandation[mood])}?page=1")
    soup = BeautifulSoup(r.text, "lxml")
    choices = list(map(lambda name: name.text, list(soup.find_all("h2", {"class": "h2_anime_title"}))))
    return choices

choices = get_recommendation_list()

while satisfied == "no":
    result = choice(choices)
    print(result)
    choices.remove(result)
    if len(choices) == 0:
        choices = get_recommendation_list()
    satisfied = input("are you satisfied : ")
