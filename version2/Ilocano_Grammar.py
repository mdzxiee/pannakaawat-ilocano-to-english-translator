import nltk

# Define the grammar using POS tags as terminal symbols
grammar_string_pos = """
    S -> NP VP | NP VP PUNC
    NP -> NN | DT NN | JJ NN | DT JJ NN | PRP | PRP PP
    NP -> DT NN | JJ NN | DT JJ NN | PRP | PRP PP
    VP -> VB | VB NP | VB PP | VB NP PP
    PP -> IN NP
    DT -> 'DT'
    NN -> 'NN'
    JJ -> 'JJ'
    VB -> 'VB'
    PRP -> 'PRP'
    IN -> 'IN'
    PUNC -> '.' | ',' | '?' | '!'
"""

class IlocanoGrammar:
    def __init__(self):
        self.ilocano_grammar = nltk.CFG.fromstring(grammar_string_pos)
        self.parser = nltk.ChartParser(self.ilocano_grammar)

    def lookup_grammar(self):
        return self.ilocano_grammar

    def lookup_grammar_parser(self):
        return self.parser