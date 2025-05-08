import nltk
from nltk.tokenize import word_tokenize
from lexicon import IlocanoLexicon
from grammar import IlocanoGrammar

def transform_tree(tree):
    if tree.label() == 'S':
        if len(tree) == 2 and tree[0].label() == 'VB' and tree[1].label() == 'NP':
            return nltk.Tree('S', [tree[1], tree[0]])
        elif len(tree) == 3 and tree[0].label() == 'VB' and tree[1].label() == 'NP' and tree[2].label() == 'NP':
            return nltk.Tree('S', [tree[1], tree[0], tree[2]])
    return tree

def get_english_sentence(transformed_tree, original_pos_tags, tokenized_words, lexicon):
    transformed_leaves = list(transformed_tree.leaves())
    indices = []
    for leaf in transformed_leaves:
        try:
            index = original_pos_tags.index(leaf)
            indices.append(index)
        except ValueError:
            pass
    english_words = []
    for idx in indices:
        ilocano_word = tokenized_words[idx]
        entry = lexicon.lookup(ilocano_word)
        if entry and 'en' in entry:
            english_words.append(entry['en'][0])
        else:
            english_words.append(ilocano_word)
    return " ".join(english_words)

def translate_to_english(ilocano_sentence, lexicon, parser):
    try:
        tokens = word_tokenize(ilocano_sentence.lower())
        pos_tags = [lexicon.lookup(token)['pos'][0] if lexicon.lookup(token) and 'pos' in lexicon.lookup(token) else token for token in tokens]
        """
            for your reference, list comprehension yung nasa taas kasi mas optimize siya kay Python
            compared sa normal na for loop na
            pos_tags = []
            for token in tokens:
                if lexicon.lookup(token) and 'pos' in lexicon.lookup(token):
                    pos_tags.append(lexicon.lookup(token)['pos'][0])
                else:   
                    pos_tags.append(token)
        """
        trees = parser.parse(pos_tags)
        for tree in trees:
            transformed_tree = transform_tree(tree)
            english_sentence = get_english_sentence(transformed_tree, pos_tags, tokens, lexicon)
            return english_sentence
        return "ayoko i translate HAHAHAHAHA."
    except Exception as e:
        return f"error nga kulet: {e}"

if __name__ == "__main__":
    ilocano_lex = IlocanoLexicon()
    grammar = IlocanoGrammar()
    parser = grammar.lookup_grammar_parser()

    ilocano_sentences = [
        "agbasa ak libro",
    ]

    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")