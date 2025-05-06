import nltk

# Define the grammar using POS tags as terminal symbols
grammar_string_pos = """
    S -> NP VP | NP VP PUNC | S CC S | UH S | UH PUNC | WP S | WRB S | WP PUNC | WRB PUNC
    S -> DT NN VBZ VBG RB | DT NNS VBZ VBG | DT NN VBZ VBG | DT NN VBZ | DT NNS VBP | DT NN VBD
    S -> DT NNS VBD | DT NN VBZ RB | DT NNS VBP RB | DT NN VBD RB | DT NNS VBD RB | DT NNS VBZ VBG RB
    S -> DT NNS VBP VBG | DT NNS VBP VBG RB | DT NN VBD VBG | DT NN VBD VBG RB | DT NNS VBD VBG | DT NNS VBD VBG RB
    S -> DT NN VBZ NP | DT NNS VBP NP | DT NN VBD NP | DT NNS VBD NP | DT NN VBZ PP | DT NNS VBP PP
    S -> DT NN VBD PP | DT NNS VBD PP | DT NN VBZ NP PP | DT NNS VBP NP PP | DT NN VBD NP PP | DT NNS VBD NP PP
    NP -> NN | NNS | NNP | DT NN | DT NNS | DT NNP | JJ NN | JJ NNS | JJ NNP | DT JJ NN | DT JJ NNS | DT JJ NNP
    NP -> JJ PART NN | JJ PART NNS | JJ PART NNP | JJS NN | JJS NNS | JJS NNP | DT JJS NN | DT JJS NNS | DT JJS NNP
    NP -> JJS PART NN | JJS PART NNS | JJS PART NNP | PRP | PRP PP | CD NN | CD NNS | DT CD NN | DT CD NNS | VBG
    NP -> NN | NNS | NNP | JJ NN | JJ NNS | JJ NNP | JJS NN | JJS NNS | JJS NNP
    VP -> VB | VBZ | VBG | VBD | VBP | VBN | VB NP | VBZ NP | VBG NP | VBD NP | VBP NP | VBN NP | VB PP | VBZ PP
    VP -> VBG PP | VBD PP | VBP PP | VBN PP | VB NP PP | VBZ NP PP | VBG NP PP | VBD NP PP | VBP NP PP | VBN NP PP
    VP -> MD VB | MD VB NP | MD VB PP | MD VB NP PP | RB VB | VB RB | VB PART JJ | RB VP
    PP -> IN NP
    DT -> 'DT'
    NN -> 'NN'
    JJ -> 'JJ'
    VB -> 'VB' | 'VBZ' | 'VBG' | 'VBD' | 'VBP' | 'VBN'
    PRP -> 'PRP'
    IN -> 'IN'
    PUNC -> '.' | ',' | '?' | '!'
    CC -> 'CC'
    PART -> 'PART'
    NNP -> 'NNP'
    RB -> 'RB'
    NNS -> 'NNS'
    WP -> 'WP'
    WRB -> 'WRB'
    JJS -> 'JJS'
    MD -> 'MD'
    UH -> 'UH'
    CD -> 'CD'
"""

class IlocanoGrammar:
    def __init__(self):
        self.ilocano_grammar = nltk.CFG.fromstring(grammar_string_pos)
        self.parser = nltk.ChartParser(self.ilocano_grammar)
    def lookup_grammar(self):
        return self.ilocano_grammar

    def lookup_grammar_parser(self):
        return self.parser