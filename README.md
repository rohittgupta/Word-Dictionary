# 📚 Word Lookup Dictionary

A simple **Python-based dictionary application** that allows users to look up word definitions.  
The project includes a graphical user interface (GUI) and a scraper for gathering word data.

---

## 🧠 Overview

**Word Lookup Dictionary** is a small offline/online hybrid word lookup desktop application written in Python.  
It provides an intuitive GUI for searching words, fetching definitions from an open dictionary API,  
and offering offline suggestions from a local dataset when the user is offline.

Built with standard Python libraries and a small scraping helper for fetching definitions from public APIs.

---

## ✨ Features

- 🖥️ **Tkinter GUI (`gui/app.py`)** with a search box and results area.  
- ⚡ **Offline support** using a local word list (`data/words.txt`) and an in-memory Trie structure.  
- 🔍 **Prefix search** for quick word completions via `core/trie.py`.  
- 🧩 **Edit-distance (Levenshtein)** based word suggestion system (`core/edit_distance.py`).  
- 🌐 **Online definition fetcher** using `requests` and an open dictionary API (`scraper/scraper.py`).  
- 🧾 **Graceful fallback** — if no online definition is found, it provides similar words or corrections.

---

## 🚀 Quickstart

### 1. Create a virtual environment (recommended) and activate it.

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the application:

```bash
python main.py
```

🪟 A small GUI window will open.

- Type a word and press Search.
- If an online definition is available, it will appear.
- Otherwise, the app will show offline suggestions or likely corrections.

## 🗂️ Project Structure

```
Word-Dictionary/
│
├── main.py                # Entry point that creates Tkinter root and launches GUI
│
├── gui/
│   └── app.py             # GUI implementation and integration with Dictionary logic
│
├── core/
│   ├── dictionary.py      # Loads local word list, fetches online definitions, and handles logic
│   ├── trie.py            # Trie data structure for prefix search and lookups
│   └── edit_distance.py   # Levenshtein distance algorithm for suggesting similar words
│
├── scraper/
│   └── scraper.py         # Helper module for querying https://api.dictionaryapi.dev
│
├── data/
│   └── words.txt          # Local word list for offline search
│
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## ⚙️ Implementation Details

- Input: A single word (string) entered through the GUI.

- Output: Online definition (if available), or offline prefix suggestions / edit-distance corrections.

- Error Handling:
  - Network/API failure: Graceful fallback to offline mode using Trie.
  - Empty input: GUI displays “No results”.
  - Timeouts: Scraper uses a 5-second timeout.
  - Large word list: Currently small for demo purposes; can be extended.

## 🧩 Dependencies

The app requires the following Python packages:

- `requests` — for calling the online dictionary API.
- `beautifulsoup4` — included in `requirements.txt` but not currently used (safe to remove).

Install them via:

```bash
pip install -r requirements.txt
```

## 🛠️ Extending the Project

You can easily build upon this project:

- 📖 Add more words to `data/words.txt` (one per line) to improve offline results.
- 🧠 Enhance `scraper/scraper.py` to include richer data such as examples or phonetics.
- ⚙️ Optimize edit-distance search by implementing a BK-tree for faster matching.
- 🧪 Add unit tests (e.g., with pytest) for Trie, EditDistance, and `Dictionary.lookup`.
- ☁️ Integrate an alternate online API or add local caching for speed.
