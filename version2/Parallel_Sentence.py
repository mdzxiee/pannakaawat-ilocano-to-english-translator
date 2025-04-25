class ParallelSentence:
    def __init__(self):
        self.map = {
            'adayo': 'long distance',
            'naimbag a bigat': 'good morning',
            'agyamanak': 'thank you',
            'ak agbasa libro': 'i read book',
            'Nasayaat, sika?': 'Fine. And you?'
        }

    def lookup_parallel(self, ilocano_input):
        return self.map.get(ilocano_input.lower())
