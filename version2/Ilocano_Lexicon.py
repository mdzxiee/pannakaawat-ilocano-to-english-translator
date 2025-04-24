class IlocanoLexicon:
    def __init__(self):
        self.lexicon = {
            'ak': {'en': ['I'], 'pos': ['PRP']},
            'ka': {'en': ['you'], 'pos': ['PRP']},
            'isuna': {'en': ['he', 'she', 'it'], 'pos': ['PRP']},
            'kami': {'en': ['we'], 'pos': ['PRP']},
            'kayo': {'en': ['you'], 'pos': ['PRP']},
            'ti': {'en': ['the'], 'pos': ['DT']},
            'dagiti': {'en': ['the'], 'pos': ['DT']},
            'maysa': {'en': ['a', 'one'], 'pos': ['DT', 'CD']},
            'balay': {'en': ['house'], 'pos': ['NN']},
            'libro': {'en': ['book'], 'pos': ['NN']},
            'aso': {'en': ['dog'], 'pos': ['NN']},
            'pusa': {'en': ['cat'], 'pos': ['NN']},
            'bassit': {'en': ['small'], 'pos': ['JJ']},
            'dakkel': {'en': ['big'], 'pos': ['JJ']},
            'napintas': {'en': ['beautiful'], 'pos': ['JJ']},
            'nalaing': {'en': ['good'], 'pos': ['JJ']},
            'agtaray': {'en': ['run'], 'pos': ['VB']},
            'agkanta': {'en': ['sing'], 'pos': ['VB']},
            'agbasa': {'en': ['read'], 'pos': ['VB']},
            'mangted': {'en': ['give'], 'pos': ['VB']},
            'ken': {'en': ['and'], 'pos': ['CC']},
            'iti': {'en': ['to', 'in', 'at'], 'pos': ['IN']},
            '.': {'en': ['.'], 'pos': ['.']},
            ',': {'en': [','], 'pos': [',']},
            '?': {'en': ['?'], 'pos': ['?']},
            'nga': {'en': [''], 'pos': ['PART']},
            'ket': {'en': ['is'], 'pos': ['VBZ']},
            'ubing': {'en': ['child'], 'pos': ['NN']},
        }

    def lookup(self, word):
        return self.lexicon.get(word.lower())