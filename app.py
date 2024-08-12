import requests

def get_joke():
    response = requests.get("https://api.punapi.com/random")
    data = response.json()
    joke = data['content']
    return joke

def main():
    # Définissez le nombre de blagues à afficher
    num_jokes = 5

    # Boucle pour obtenir et afficher plusieurs blagues
    for _ in range(num_jokes):
        joke = get_joke()
        print(f"Joke: {joke}")
        print("-" * 30)  # Ligne de séparation entre les blagues

if __name__ == "__main__":
    main()
