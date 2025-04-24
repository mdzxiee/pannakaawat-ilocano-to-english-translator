import re
from nltk.tokenize import word_tokenize

from Ilocano_Lexicon import IlocanoLexicon
from Parallel_Sentence import ParallelSentence
from Ilocano_Grammar import IlocanoGrammar

def translate_to_english(ilocano_sentence, lexicon, parallel_sentence, parser):
    try:
        parallel_translation = parallel_sentence_translator_to_en(parallel_sentence, ilocano_sentence)
        print(parallel_translation)
        if is_fully_translated(parallel_translation, lexicon):
            return parallel_translation
        else:
            tokenized_words, pos_tags = tokenize_and_tag(parallel_translation, lexicon)
            trees = parser.parse(pos_tags)
            grammar_based_translation = grammar_based_translator_to_en(tokenized_words, lexicon, trees)
            if not grammar_based_translation:
                return "Translation not possible based on the current grammar and lexicon."
            return grammar_based_translation

    except ValueError as ex:
        return f"Error during parsing: {ex}"

def is_fully_translated(parallel_translation, lexicon):
    tokens = word_tokenize(parallel_translation.lower())
    for token in tokens:
        word = lexicon.lookup(token)
        if not (word and 'en' in word) and token not in ['.', ',', '?', '!']:
            return True
    return False

def parallel_sentence_translator_to_en(parallel_sentence, ilocano_sentence):
    sent = ilocano_sentence
    for ilocano_phrase, english_phrase in parallel_sentence.map.items():
        pattern = r'\b' + re.escape(ilocano_phrase) + r'\b'
        if re.search(pattern, sent):
            sent = re.sub(pattern, english_phrase, sent)
    return sent

def grammar_based_translator_to_en(tokenized_words, lexicon, trees):
    try:
        translations = []

        for tree in trees:
            english_tokens = []
            for index, leaf in enumerate(tree.leaves()):
                # Python construct used to iterate over the leaf nodes of a parse tree (tree) while also keeping track of the index of each leaf.
                ilocano_word = tokenized_words[index]
                token = lexicon.lookup(ilocano_word)

                if token and 'en' in token:
                    english_tokens.append(token['en'][0])
                else:
                    english_tokens.append(ilocano_word)  # Keep original if no translation
            translations.append(" ".join(english_tokens))

        if translations:
            return translations[0]  # Return the first possible translation
        else:
            return "Translation not possible based on the current grammar."

    except ValueError as ex:
        return f"Error during parsing: {ex}"


def tokenize_and_tag(ilocano_sentence, lexicon):
    tokens = word_tokenize(ilocano_sentence.lower())
    pos_tags = []
    ilocano_words = []

    for token in tokens:
        word = lexicon.lookup(token)
        ilocano_words.append(token)
        if word and 'pos' in word:
            pos_tags.append(word['pos'][0])
        else:
            pos_tags.append(token)

    return ilocano_words, pos_tags

ilocano_lex = IlocanoLexicon()
parallel_translations = ParallelSentence()

grammar = IlocanoGrammar()
grammar_parser = grammar.lookup_grammar_parser()

# Example Ilocano sentences
ilocano_sentences = [
    "ak agbasa libro.",
    "ti bassit nga aso.",
    "isuna agkanta.",
    "dagiti dakkel a balay.",
    "kami mangted libro iti ka.",
    "ka agtaray.",
    "maysa napintas a pusa." #Error to sa production rules
]

print("--- POS-Tagged Grammar-Based Translation with Special Lexicon ---")
for sentence in ilocano_sentences:
    english_translation = translate_to_english(sentence, ilocano_lex, parallel_translations, grammar_parser)
    print(f"Ilocano: {sentence}")
    print(f"English: {english_translation}\n")


