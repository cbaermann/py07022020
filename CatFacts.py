import requests
import random

def main():
    request_catfact = requests.get("https://cat-fact.herokuapp.com/facts")

    listOfFacts = request_catfact.json()

    random_fact = random.choice(listOfFacts["all"])

    print(random_fact["text"])

    # for catfact in request_catfact.json()["all"]:
    #     print(catfact.get("text"))
main()
