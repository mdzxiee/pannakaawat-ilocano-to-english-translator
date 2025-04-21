"""
Algorithm:
    1) Tokenize the Ilocano Sentence
    2) POS Tag the Tokenized Sentence
    3) Use the Production Rules of the CFG
            3.1) Production Rules for Valid Sentences (Terminal Symbols)
            3.2) Production Rules for the Non-Terminal Symbols
    4) Check each word/article/punctuation on the Lexicon and append each to the translation
    5) Return the translation
"""

import nltk
from nltk.tokenize import word_tokenize

grammar_string = """
    S -> NP VP | NP VP PUNC
    NP -> N | Det N | JJ N | Det JJ N | PN | PN PP
    NP -> Det N | JJ N | Det JJ N | PN | PN PP
    VP -> V | V NP | V PP | V NP PP
    PP -> P NP
    Det -> 'ti' | 'dagiti' | 'maysa'
    N -> 'balay' | 'libro' | 'aso' | 'pusa'
    JJ -> 'bassit' | 'dakkel' | 'napintas' | 'nalaing'
    V -> 'agtaray' | 'agkanta' | 'agbasa' | 'mangted'
    PN -> 'ak' | 'ka' | 'isuna' | 'kami' | 'kayo'
    P -> 'iti'
    PUNC -> '.' | ',' | '?'
"""

# ilocano_lexicon = {
#     'ilocano word/phrase': 'english translation',
#     '.': '.',
#     ',': ',',
#     '?': '?',
#     '!': '!'
# }

ilocano_lexicon = {
    'ak': 'I',
    'ka': 'you',
    'isuna': 'he', 'isuna': 'she', 'isuna': 'it',
    'kami': 'we',
    'kayo': 'you', # Plural
    'dagiti': 'the',  # Plural definite article
    'ti': 'the',      # Singular definite article
    'maysa': 'a', 'maysa': 'an', 'maysa': 'one',
    'balay': 'house',
    'libro': 'book',
    'aso': 'dog',
    'pusa': 'cat',
    'bassit': 'small',
    'dakkel': 'big',
    'napintas': 'beautiful',
    'nalaing': 'good',
    'agtaray': 'runs',
    'agkanta': 'sings',
    'agbasa': 'reads',
    'mangted': 'gives',
    'ken': 'and',
    'nga': 'is',
    '.': '.',
    ',': ',',
    '?': '?'
}

ilocano_grammar = nltk.CFG.fromstring(grammar_string)
parser = nltk.ChartParser(ilocano_grammar)

"""
    Translates simple declarative Ilocano sentences/phrases to English using a
    context-free grammar.
"""
def translate_to_english(ilocano_sentence):
    tokens = word_tokenize(ilocano_sentence)

    try:
        trees = parser.parse(tokens)
        translations = []

        for tree in trees:
            english_tokens = []
            for leaf in tree.leaves():
                if leaf in ilocano_lexicon:
                    english_tokens.append(ilocano_lexicon[leaf])
                else:
                    english_tokens.append(leaf)

            translations.append(" ".join(english_tokens))

        if translations:
            return translations[0] # Return the first possible translation
        else:
            return "Translation not possible based on the current grammar."

    except ValueError as e:
        return f"Error during parsing: {e}"
# End of translate_to_english()

# Example Ilocano sentences/phrases (kinuha ko lang sa google, diko alam if tama)
ilocano_phrases = [
    "ak agbasa libro.",
    "ti bassit nga aso.",
    "isuna agkanta.",
    "dagiti dakkel a balay.",
    "kami mangted libro iti ka.",
    "ka agtaray.",
    "maysa napintas a pusa."
]

# Translate and print the results
for phrase in ilocano_phrases:
    english_translation = translate_to_english(phrase)
    print(f"Ilocano: {phrase}\nEnglish: {english_translation}\n")
