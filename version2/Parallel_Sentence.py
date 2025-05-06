class ParallelSentence:
    def __init__(self):
        self.map = {
            'naimbag a bigat': 'good morning',
            'agyamanak': 'thank you',
            'nasayaat, sika': 'fine, and you?',
        }

    def lookup_parallel(self, ilocano_input):
        return self.map.get(ilocano_input.lower())
