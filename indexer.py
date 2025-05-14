import json
import re
from collections import defaultdict

INDEX_PATH = "index.json"

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def build_index(pages):
    index = defaultdict(dict)  # word -> {url: frequency}
    
    for url, content in pages.items():
        tokens = tokenize(content)
        for word in tokens:
            index[word][url] = index[word].get(url, 0) + 1
    return index

def save_index(index, path=INDEX_PATH):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f)

def load_index(path=INDEX_PATH):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def print_word(index, word):
    word = word.lower()
    if word in index:
        print(f"Inverted index for '{word}':")
        for url, freq in index[word].items():
            print(f"  {url} → {freq} times")
    else:
        print(f"'{word}' not found in index.")

def find_phrase(index, phrase):
    words = tokenize(phrase)
    if not words:
        return []
    
    sets = []
    for word in words:
        if word in index:
            sets.append(set(index[word].keys()))
        else:
            sets.append(set())
    
    result = set.intersection(*sets)
    return list(result)
