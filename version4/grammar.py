import nltk

grammar_string_ilocano = """
S -> VB NP | VB NP NP
NP -> PRP | NN | NNS | DT NN | DT NNS | JJ NN | JJ NNS
VB -> 'VB'
PRP -> 'PRP'
NN -> 'NN'
NNS -> 'NNS'
DT -> 'DT'
JJ -> 'JJ'
"""

class IlocanoGrammar:
    def __init__(self):
        self.ilocano_grammar = nltk.CFG.fromstring(grammar_string_ilocano)
        self.parser = nltk.ChartParser(self.ilocano_grammar)
    
    def lookup_grammar(self):
        return self.ilocano_grammar
    
    def lookup_grammar_parser(self):
        return self.parser