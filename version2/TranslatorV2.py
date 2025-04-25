import re
from nltk.tokenize import word_tokenize

from Ilocano_Lexicon import IlocanoLexicon
from Parallel_Sentence import ParallelSentence
from Ilocano_Grammar import IlocanoGrammar

def translate_to_english(ilocano_sentence, lexicon, parallel_sentence, parser):
    """
    This method translates a source language sentence to english
    using the parallel language translations, the grammar production rules, and the lexicon.
    :param ilocano_sentence: input or source language sentence to be translated to english
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :param parallel_sentence: parallel sentences of ilocano to english translations
    :param parser: analyze and find a sequence of POS tags conforming to the defined grammar
    :return: translated version of the source language sentence
    from the parallel translation and grammar based translation of the sentence
    """
    try:
        parallel_translation = parallel_sentence_translator_to_en(parallel_sentence, ilocano_sentence)

        if is_fully_translated(parallel_translation, lexicon):
            return parallel_translation
        else:
            tokenized_words, pos_tags = tokenize_and_tag(parallel_translation, lexicon)
            trees = parser.parse(pos_tags)  # Finds a sequence of POS tags conforming to the defined grammar
            grammar_based_translation = grammar_based_translator_to_en(tokenized_words, lexicon, trees)
            if not grammar_based_translation:
                return "Translation not possible based on the current grammar and lexicon."
            return grammar_based_translation

    except ValueError as ex:
        return f"Error during parsing: {ex}"

def is_fully_translated(parallel_translation, lexicon):
    """
    This method checks and return a boolean value if a given sentence or translation is fully translated to english
    :param parallel_translation: input sentence or initial translation to be checked
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :return: boolean true or false
    """
    tokens = word_tokenize(parallel_translation.lower())
    for token in tokens:
        word = lexicon.lookup(token)
        if not (word and 'en' in word) and token not in ['.', ',', '?', '!']:
            return True
    return False

def parallel_sentence_translator_to_en(parallel_sentence, ilocano_sentence):
    """
    This method translates a source language sentence to english
    using the predefined parallel english translations of simple Ilocano sentences and phrases
    :param parallel_sentence: parallel sentences of ilocano to english translations
    :param ilocano_sentence: input or source language sentence to be translated to english
    :return: translated version of the source language sentence from the parallel translation of sentences
    """
    sent = ilocano_sentence
    for ilocano_phrase, english_phrase in parallel_sentence.map.items():
        pattern = r'\b' + re.escape(ilocano_phrase) + r'\b'
        if re.search(pattern, sent):
            sent = re.sub(pattern, english_phrase, sent)
    return sent

def grammar_based_translator_to_en(tokenized_words, lexicon, trees):
    """
    This method translates a source language sentence to english
    using the Ilocano language lexicon
    :param tokenized_words: tokenized source language sentence
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :param trees: tree structure of the grammar having the tokenized sentence with their POS Tag
    :return: translated version of the source language sentence using the lexicon and the grammar production rules
    """
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
    """
    This method tokenize a given string and check their corresponding POS tag from the lexicon, thus,
    return the tokenized sentence and the POS tag of each token
    :param ilocano_sentence: input or source language sentence to be tokenized and to be POS tagged
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :return: tokenized source language sentence, and their corresponding POS Tags
    """
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


if __name__ == "__main__":
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
        "maysa napintas a pusa.", #Error to sa production rules
        "Nasayaat, sika?" # Part din siguro ng limitations natin yung processing nung may mga punctuations in the middle
    ]

    print("--- POS-Tagged Grammar-Based Translation with Special Lexicon ---")
    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parallel_translations, grammar_parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")


