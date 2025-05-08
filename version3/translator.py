import re
from nltk.tokenize import word_tokenize

from lexicon import IlocanoLexicon
from parallel_sentence import ParallelSentence
from grammar import EnglishGrammar

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
    sent = ilocano_sentence.lower()
    for ilocano_phrase, english_phrase in parallel_sentence.map.items():
        pattern = r'\b' + re.escape(ilocano_phrase) + r'\b'
        if re.search(pattern, sent):
            sent = re.sub(pattern, english_phrase, sent)
    return sent

def grammar_based_translator_to_en(tokenized_words, lexicon, trees):
    """
    This method translates a source language sentence to english
    using the Ilocano language lexicon and arranges it to active voice
    :param tokenized_words: tokenized source language sentence
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :param trees: tree structure of the grammar having the tokenized sentence with their POS Tag
    :return: translated version of the source language sentence in active voice
    """
    try:
        translations = []
        for tree in trees:
            english_tokens = []
            word_pos_pairs = []
            for index, leaf in enumerate(tree.leaves()):
                ilocano_word = tokenized_words[index]
                token = lexicon.lookup(ilocano_word)
                if token and 'en' in token and 'pos' in token:
                    english_tokens.append(token['en'][0])
                    word_pos_pairs.append((token['en'][0], token['pos'][0]))
                elif token and 'en' in token:
                    english_tokens.append(token['en'][0])
                    word_pos_pairs.append((token['en'][0], None)) # Handle cases without POS
                else:
                    english_tokens.append(ilocano_word)
                    word_pos_pairs.append((ilocano_word, None)) # Keep original if no translation

            subject = ""
            verb = ""
            obj = ""
            others = []

            # Prioritize Pronouns (PRP) as potential subjects
            for word, pos in word_pos_pairs:
                if pos == 'PRP' and not subject:
                    subject = word
                    break # Take the first pronoun as the subject for simplicity

            # Then look for nouns (N*) as subject if no pronoun is found
            if not subject:
                for word, pos in word_pos_pairs:
                    if pos and pos.startswith('N'):
                        subject = word
                        break

            # Identify the verb (V*)
            for word, pos in word_pos_pairs:
                if pos and pos.startswith('V') and not verb:
                    verb = word
                    break

            # Identify the object (N*) - after the verb
            verb_found = False
            for word, pos in word_pos_pairs:
                if pos and pos.startswith('V'):
                    verb_found = True
                elif verb_found and pos and pos.startswith('N') and not obj:
                    obj = word
                elif not (pos == 'PRP' or (pos and pos.startswith('N')) or (pos and pos.startswith('V'))):
                    others.append(word)

            active_voice_translation = " ".join([subject, verb, obj, " ".join(others)]).strip().replace("  ", " ")
            translations.append(active_voice_translation)

        if translations:
            return translations[0]  # Return the first possible translation
        else:
            return "Translation not possible based on the current grammar."

    except ValueError as ex:
        return f"Error during parsing: {ex}"


def tokenize_and_tag(ilocano_sentence, lexicon):
    """
    This method tokenizes a given string, checks their corresponding POS tag from the lexicon,
    rearranges the POS tags into a basic active voice order (Subject-Verb-Object),
    and returns the tokenized sentence and the rearranged POS tags.
    :param ilocano_sentence: input or source language sentence to be tokenized and POS tagged
    :param lexicon: collection of words in a source language,
    their corresponding translations in the target language, and Part-of-Speech (POS) tag
    :return: tokenized source language sentence, and their corresponding rearranged POS Tags
    """
    tokens = word_tokenize(ilocano_sentence.lower())
    pos_tags = []
    ilocano_words = []

    word_pos_list = []
    for token in tokens:
        word = lexicon.lookup(token)
        ilocano_words.append(token)
        if word and 'pos' in word:
            word_pos_list.append((token, word['pos'][0]))
            pos_tags.append(word['pos'][0]) # Keep original word for now
        else:
            word_pos_list.append((token, token)) # Tag with the word itself if no POS
            pos_tags.append(token) # Keep original word for now

    # Basic rearrangement logic for POS tags
    subject_pos = None
    verb_pos = None
    object_pos = None
    other_pos_tags = []
    rearranged_pos_tags = []

    # Prioritize PRP as subject
    for word, pos in word_pos_list:
        if pos == 'PRP' and not subject_pos:
            subject_pos = pos
            rearranged_pos_tags.append(pos)
            break

    # Then look for N* as subject
    if not subject_pos:
        for word, pos in word_pos_list:
            if pos and pos.startswith('N') and not subject_pos:
                subject_pos = pos
                rearranged_pos_tags.append(pos)
                break

    # Identify verb (V*)
    for word, pos in word_pos_list:
        if pos and pos.startswith('V') and not verb_pos:
            verb_pos = pos
            rearranged_pos_tags.append(pos)
            break

    # Identify object (N*) after verb
    verb_found_index = -1
    for i, (word, pos) in enumerate(word_pos_list):
        if pos and pos.startswith('V'):
            verb_found_index = i
            break

    if verb_found_index != -1:
        for i in range(verb_found_index + 1, len(word_pos_list)):
            word, pos = word_pos_list[i]
            if pos and pos.startswith('N') and not object_pos:
                object_pos = pos
                rearranged_pos_tags.append(pos)
                break

    # Add any remaining POS tags
    for pos in pos_tags:
        if pos not in rearranged_pos_tags:
            rearranged_pos_tags.append(pos)

    return ilocano_words, rearranged_pos_tags

if __name__ == "__main__":
    ilocano_lex = IlocanoLexicon()
    parallel_translations = ParallelSentence()

    grammar = EnglishGrammar()
    grammar_parser = grammar.lookup_grammar_parser()

    # Example Ilocano sentences
    ilocano_sentences = [
        "agbasa ak libro",
    ]

    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parallel_translations, grammar_parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")