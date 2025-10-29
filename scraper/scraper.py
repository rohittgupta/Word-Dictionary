import requests

def get_definition(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url, timeout=5) #setting the time thinking limit to 5 second then it will get down to exception output..

        if response.status_code != 200:
            return "Definition not found."

        data = response.json()
        meaning = data[0]["meanings"][0]["definitions"][0]["definition"] #saying first definition ..
        return meaning
    except Exception:
        return "Definition not found."
