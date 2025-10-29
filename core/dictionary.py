from core.trie import Trie
from core.edit_distance import suggest_corrections
from scraper.scraper import get_definition

class Dictionary:
    def __init__(self, words_file="data/words.txt"):#constructor call..self
        self.trie = Trie()
        self.words = []
        self.load_words(words_file)

    def load_words(self, file):#extraction from the file ..
        with open(file, "r") as f:
            for word in f:
                word = word.strip().lower()
                self.words.append(word)
                self.trie.insert(word)

    def lookup(self, word):#lookup to find defination part..
        word = word.lower()

        # Always try to fetch definition (even if not in words.txt)
        definition = get_definition(word)
        if "not found" not in definition.lower() and "error" not in definition.lower():
            return {"word": word, "definition": definition}

        # If API fails, fallback to Trie suggestions/corrections ..
        if self.trie.search(word):
            return {"word": word, "definition": "Definition not available (try again later)."}
        
        #suggestion ..
        suggestions = self.trie.starts_with(word)
        if suggestions:
            return {"suggestions": suggestions[:5]}

        #corrections ..
        corrections = suggest_corrections(word, self.words)
        return {"corrections": corrections[:5]}
