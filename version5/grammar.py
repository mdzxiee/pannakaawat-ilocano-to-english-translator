import nltk

grammar_string_ilocano = """
# Sentence Structures: Declarative Only (SV, SVO, SVC) 
S -> NP VP
S -> VP NP
S -> NP VB NP
S -> NP VB
S -> JJ NP
S -> RB VP
S -> VP RB
S -> NP JJ

# Verb-initial (common in Ilocano)
S -> VB NP | VBD NP | VBG NP | VBP NP | VBZ NP
S -> VB PP | VBD PP | VBG PP | VBP PP | VBZ PP
S -> VB NP PP | VBD NP PP | VBG NP PP | VBP NP PP | VBZ NP PP
S -> VB NP NP | VBD NP NP | VBG NP NP | VBP NP NP | VBZ NP NP
S -> NP VP
VP -> VBZ NP  

# Verb Phrase for Future Tense
VP -> MD VB | MD VB NP | MD VB PP
VP -> VBP NP | VBG NP | VBZ NP
VP -> MD VB | MD VBD

# Verb Phrases for Continuous Actions
VP -> MD VBZ NP           
VP -> MD VBG NP            
VP -> VBZ RB NP            
VP -> VBG NP               

# Noun Phrases
NP -> DT NN | DT NNS | DT NN | DT NNS
NP -> JJ NN | JJ NNS
NP -> PRP | PRP PP | PRPS NN | PRPS NNS
NP -> DT NN PRPS | DT NNS PRPS | PRPS NN PRPS | PRPS NNS PRPS

# Adjective-initial Declaratives (Updated for Reordering)
S -> JJ DT NN | JJ DT NNS | JJ NN | JJ NNS
S -> JJ NP | JJ PP
S -> JJ NN PRPS | JJ NNS PRPS | JJ DT NN PRPS | JJ DT NNS PRPS
S -> JJ DT NN PRP | JJ NN PRP | JJ DT NNS PRP
S -> JJ DT NN PRPS         
S -> DT NN VBZ JJ          
S -> PRPS NN VBZ JJ        
S -> NN DT VBD             
S -> DT NN VBD             
S -> JJ DT NN 

# Additional Simple Constructions 
S -> NP VP PP
S -> NP DT VP
S -> JJ DT NN
S -> NP VP RB
S -> VP NP RB
S -> NP VP NP
S -> NP VP ADJP
S -> NP VP NP

# Phrase Structures
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
NP -> PRPS NN             
NP -> NN PRPS              
NP -> DT NN PRPS   

# Verb Phrases
VP -> VB | VBZ | VBG | VBD | VBP | VBN 
VP -> VB NP | VBZ NP | VBG NP | VBD NP | VBP NP | VBN NP 
VP -> VB PP | VBZ PP | VBG PP | VBD PP | VBP PP | VBN PP
VP -> VB NP PP | VBZ NP PP | VBG NP PP | VBD NP PP | VBP NP PP | VBN NP PP
VP -> MD VB | MD VB NP | MD VB PP | MD VB NP PP 
VP -> RB VB | VB RB | RB VB NP | VB NP RB
VP -> VB VP RB
VP -> VB NP VP
VP -> MD VB         
VP -> VBG NP         
        

# Prepositional Phrases
PP -> IN NP | IN NN | IN NNS | IN NNP | IN PRP

# Adjective Phrases
ADJP -> JJ | JJ PP | RB JJ | JJ RB | JJS | JJS PP | RB JJS | JJS RB

# Adverb Phrases
ADVP -> RB | RB PP | RB RB

# Punctuation Handling
PUNC -> ',' | '.' | '?' | '!'
S -> S PUNC  
S -> S PUNC S  

# --- Terminal Symbols ---
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
JJS -> 'JJS'
MD -> 'MD'
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
