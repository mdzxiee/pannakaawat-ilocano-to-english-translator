import nltk

# Define the grammar using POS tags as terminal symbols
grammar_string_pos = """
    S -> NP VP | NP VP PUNC | S CC S | UH S | UH PUNC | WP S | WRB S | WP PUNC | WRB PUNC
    NP -> NN | NNS | NNP
    NP -> DT NN | DT NNS | DT NNP
    NP -> JJ NN | JJ NNS | JJ NNP
    NP -> DT JJ NN | DT JJ NNS | DT JJ NNP
    NP -> JJ PART NN | JJ PART NNS | JJ PART NNP
    NP -> JJS NN | JJS NNS | JJS NNP
    NP -> DT JJS NN | DT JJS NNS | DT JJS NNP
    NP -> JJS PART NN | JJS PART NNS | JJS PART NNP
    NP -> PRP
    NP -> PRP PP
    NP -> CD NN | CD NNS
    NP -> DT CD NN | DT CD NNS
    NP -> VBG
    NP -> PRP$ NN | PRP$ NNS | PRP$ NNP
    NP -> PRP$ JJ NN | PRP$ JJ NNS | PRP$ JJ NNP
    NP -> PRP$ JJS NN | PRP$ JJS NNS | PRP$ JJS NNP
    VP -> VB | VBZ | VBG | VBD | VBP | VBN
    VP -> VB NP | VBZ NP | VBG NP | VBD NP | VBP NP | VBN NP
    VP -> VB PP | VBZ PP | VBG PP | VBD PP | VBP PP | VBN PP
    VP -> VB NP PP | VBZ NP PP | VBG NP PP | VBD NP PP | VBP NP PP | VBN NP PP
    VP -> MD VB | MD VB NP | MD VB PP | MD VB NP PP
    VP -> RB VB | VB RB
    VP -> VB PART JJ
    VP -> RB VP
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
    PRP$ -> 'PRP$'
"""

class IlocanoGrammar:
    def __init__(self):
        self.ilocano_grammar = nltk.CFG.fromstring(grammar_string_pos)
        self.parser = nltk.ChartParser(self.ilocano_grammar)
    def lookup_grammar(self):
        return self.ilocano_grammar

    def lookup_grammar_parser(self):
        return self.parser