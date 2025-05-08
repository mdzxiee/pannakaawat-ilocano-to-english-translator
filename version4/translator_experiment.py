import nltk
from nltk.tokenize import word_tokenize
from lexicon import IlocanoLexicon
from grammar import IlocanoGrammar

def transform_tree(tree):
    if tree.label() == 'S':
        if len(tree) == 2 and tree[0].label() == 'VB' and tree[1].label() == 'NP':
            vb = tree[0][0]
            np = tree[1]
            np_leaf = np[0] if len(np) == 1 else np[1]
            return (np_leaf, vb)
        elif len(tree) == 3 and tree[0].label() == 'VB' and tree[1].label() == 'NP' and tree[2].label() == 'NP':
            vb = tree[0][0]
            subj = tree[1]
            obj = tree[2]
            subj_leaf = subj[0] if len(subj) == 1 else subj[1]
            obj_leaf = obj[0] if len(obj) == 1 else obj[1]
            return (subj_leaf, vb, obj_leaf)
        elif len(tree) == 2 and tree[0].label() == 'JJ' and tree[1].label() == 'NP':
            jj = tree[0][0]
            np = tree[1]
            np_leaf = np[0] if len(np) == 1 else np[1]
            return (np_leaf, 'is', jj)
    return tree

def get_english_sentence(transformed_tree, original_pos_tags, tokenized_words, lexicon):
    if isinstance(transformed_tree, tuple):
        elements = transformed_tree
        english_words = []
        for elem in elements:
            if elem == 'is':
                english_words.append('is')
            else:
                try:
                    token_idx = original_pos_tags.index(elem)
                    ilocano_word = tokenized_words[token_idx]
                    entry = lexicon.lookup(ilocano_word)
                    if entry and 'en' in entry:
                        english_word = entry['en'][0]
                    else:
                        english_word = ilocano_word
                except ValueError:
                    english_word = elem
                english_words.append(english_word)

        if len(elements) == 2:
            subject, verb = english_words
            return f"{subject} {verb}"
        elif len(elements) == 3:
            if elements[1] == 'is':
                np, _, jj = english_words
                if original_pos_tags[original_pos_tags.index(elements[0])] in ['DT NN', 'DT NNS']:
                    np = f"the {np}"
                return f"{np} is {jj}"
            else:
                subject, verb, obj = english_words
                if original_pos_tags[original_pos_tags.index(elements[2])] == 'NN':
                    obj = f"a {obj}"
                return f"{subject} will {verb} {obj}"
    return " ".join(str(leaf) for leaf in transformed_tree.leaves())

def translate_to_english(ilocano_sentence, lexicon, parser):
    try:
        tokens = word_tokenize(ilocano_sentence.lower())
        pos_tags = [lexicon.lookup(token)['pos'][0] if lexicon.lookup(token) and 'pos' in lexicon.lookup(token) else token for token in tokens]
        trees = list(parser.parse(pos_tags))
        for tree in trees:
            transformed_tree = transform_tree(tree)
            english_sentence = get_english_sentence(transformed_tree, pos_tags, tokens, lexicon)
            return english_sentence
        return "Translation not possible."
    except Exception as e:
        return f"Error during parsing: {e}"

if __name__ == "__main__":
    ilocano_lex = IlocanoLexicon()
    grammar = IlocanoGrammar()
    parser = grammar.lookup_grammar_parser()

    ilocano_sentences = [
        "agbasa ak libro",
        "nagtakki ka",
        "nasadot ti aso"
    ]

    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")