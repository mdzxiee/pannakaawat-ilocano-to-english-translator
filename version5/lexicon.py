import json

class IlocanoLexicon:
    def __init__(self, data_file="ilocano_lexicon.json"):
        self.data_file = data_file
        self.lexicon = self._load_lexicon()

    def _load_lexicon(self):
        """Loads the lexicon data from the JSON file."""
        lexicon_data = {}
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                lexicon_data = json.load(f)
        except FileNotFoundError:
            print(f"Error: Lexicon data file '{self.data_file}' not found.")
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{self.data_file}'.")
        return lexicon_data

    def lookup(self, word):
        """Looks up a word in the lexicon."""
        return self.lexicon.get(word.lower())

    def add_entry(self, ilocano_word, entry_data):
        """Adds a new entry to the lexicon or updates an existing one.
        for instance, ilocano_lex.add_entry("nasantuan", {"en": ["holy"], "pos": ["JJ"]})
        """
        self.lexicon[ilocano_word.lower()] = entry_data
        self._save_lexicon()

    def _save_lexicon(self):
        """Saves the lexicon data back to the JSON file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.lexicon, f, indent=2, ensure_ascii=False)
        except IOError:
            print(f"Error: Could not save lexicon data to '{self.data_file}'.")