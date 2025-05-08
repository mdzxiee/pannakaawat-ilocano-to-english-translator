import nltk

grammar_string_ilocano = """
# Sentence structures
S -> NP VP | VP NP | JJ NP | RB VP | VP RB | NP JJ
S -> S PUNC | S CC S | UH S | UH PUNC 
S -> WP VP | WRB VP | WP NP VP | WRB NP VP
S -> DT NN VB | DT NNS VB | DT NN VBD | DT NNS VBD
S -> DT NN VBZ JJ | DT NNS VBP JJ | DT NN VBD JJ | DT NNS VBD JJ
S -> VB DT NN | VBD DT NN | VB DT NNS | VBD DT NNS
S -> JJ DT NN | JJ DT NNS | JJ NNP
S -> JJ PUNC PRP | JJ PRP
S -> DT NN DT VB | NP DT VB
S -> NP S | NP VP | NP VB NP | NP VB
S -> DT VB PRP | DT VB NP | DT NP VB
S -> DT NN DT VB | DT NP VB | NP DT VB
S -> PRP | JJ PRP | JJ PUNC PRP

# Verb-initial constructions
S -> VB NP | VBD NP | VBG NP | VBP NP | VBZ NP
S -> VB PP | VBD PP | VBG PP | VBP PP | VBZ PP
S -> VB NP PP | VBD NP PP | VBG NP PP | VBP NP PP | VBZ NP PP
S -> VB NP NP | VBD NP NP | VBG NP NP | VBP NP NP | VBZ NP NP

# Adjective-initial constructions
S -> JJ DT NN | JJ NN | JJ NP | JJ DT NNS
S -> JJ PP | JJ NP PP
S -> JJ DT NN PRPS | JJ NN PRPS | JJ DT NNS PRPS
S -> JJ DT NN PRP | JJ NN PRP | JJ DT NNS PRP
S -> DT NN DT VB | NN DT VB | DT NP VB
S -> DT NN PRP VB DT | DT NP CC DT | DT NP S
S -> VP RB | VB RB RB
S -> NP DT VP | NP DT NP VP | NP VP PP

# Questions
S -> WP VB | WP VBD | WP VBZ | WP VBP | WRB VB | WRB VBD | WRB VBZ | WRB VBP
S -> WP NP VB | WRB NP VB | WP PP | WRB PP
S -> WP JJ | WRB JJ | WP JJ NP | WRB JJ NP

# Adverbial constructions
S -> RB S | S RB | RB VP NP | VP NP RB | VP RB NP

# Noun phrases
NP -> NN | NNS | NNP 
NP -> DT NN | DT NNS | DT NNP 
NP -> JJ NN | JJ NNS | JJ NNP | DT JJ NN | DT JJ NNS | DT JJ NNP
NP -> PRP | PRP PP | PRPS NN | PRPS NNS | PRPS JJ NN | PRPS JJ NNS
NP -> CD NN | CD NNS | DT CD NN | DT CD NNS
NP -> NP CC NP | NP PP
NP -> VBG | VBG NN | VBG NP
NP -> NN PRPS | NNS PRPS | DT NN PRPS | DT NNS PRPS
NP -> JJ NN PRPS | JJ NNS PRPS | DT JJ NN PRPS | DT JJ NNS PRPS
NP -> DT VB | DT VBD | DT VBG
NP -> DT VB | DT VBD | DT VBG

# Verb phrases
VP -> VB | VBZ | VBG | VBD | VBP | VBN 
VP -> VB NP | VBZ NP | VBG NP | VBD NP | VBP NP | VBN NP 
VP -> VB PP | VBZ PP | VBG PP | VBD PP | VBP PP | VBN PP
VP -> VB NP PP | VBZ NP PP | VBG NP PP | VBD NP PP | VBP NP PP | VBN NP PP
VP -> MD VB | MD VB NP | MD VB PP | MD VB NP PP 
VP -> RB VB | VB RB | RB VB NP | VB NP RB
VP -> VB S | VB VP RB
VP -> VB PRPS VP | VB PRPS VB
VP -> VB VB | VB VP | VB NP VP
VP -> VB VB | VB NP VB | VB PRPS VB
VP -> VB PRPS DT VB | VB DT VB | VB NP NP

# Prepositional phrases
PP -> IN NP | IN NN | IN NNS | IN NNP | IN PRP

# Adjective phrases
ADJP -> JJ | JJ PP | RB JJ | JJ RB | JJS | JJS PP | RB JJS | JJS RB

# Adverb phrases
ADVP -> RB | RB PP | RB RB

S -> VB | VBD | VBG | VBZ | VBP | VBN | NN | NNS | NNP | JJ | RB

# Terminal symbols
DT -> 'DT'
NN -> 'NN'
NNS -> 'NNS'
NNP -> 'NNP'
JJ -> 'JJ'
VB -> 'VB'
VBZ -> 'VBZ'
VBG -> 'VBG'
VBD -> 'VBD'
VBP -> 'VBP'
VBN -> 'VBN'
PRP -> 'PRP'
PRPS -> 'PRP$'
IN -> 'IN'
PUNC -> '.' | ',' | '?' | '!'
CC -> 'CC'
RB -> 'RB'
WP -> 'WP'
WRB -> 'WRB'
JJS -> 'JJS'
MD -> 'MD'
UH -> 'UH'
CD -> 'CD'
"""

class IlocanoGrammar:
    def __init__(self):
        self.ilocano_grammar = nltk.CFG.fromstring(grammar_string_ilocano)
        self.parser = nltk.ChartParser(self.ilocano_grammar)
    
    def lookup_grammar(self):
        return self.ilocano_grammar
    
    def lookup_grammar_parser(self):
        return self.parser