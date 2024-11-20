import requests

def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    return data

def main():
    # Définissez le nombre de blagues à afficher
    num_jokes = 5

    # Boucle pour obtenir et afficher plusieurs blagues
    for _ in range(num_jokes):
        joke = get_joke()
        jokeAsk = joke['setup']
        jokeRep = joke['punchline']
        print(f"Joke: {jokeAsk},\nPunchline: {jokeRep}")
        print("-" * 30)  # Ligne de séparation entre les blagues

if __name__ == "__main__":
    main()
