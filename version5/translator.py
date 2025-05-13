import nltk

from nltk.tokenize import word_tokenize
from lexicon import IlocanoLexicon
from grammar import IlocanoGrammar

def transform_tree(tree):
    if tree.label() == 'S':
        if len(tree) == 2 and tree[0].label() == 'VB' and tree[1].label() == 'NP':
            return nltk.Tree('S', [tree[1], tree[0]])
        elif len(tree) == 3 and tree[0].label() == 'VB' and tree[1].label() == 'NP' and tree[2].label() == 'NP':
            sub_tree = tree[1]
            if len(sub_tree) == 1 and sub_tree[0].label() == 'PRP':
                return nltk.Tree('S', [sub_tree, tree[0], tree[2]])
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
            # If no translation is found, use the original word
            english_words.append(ilocano_word)
    return " ".join(english_words)

def translate_to_english(ilocano_sentence, lexicon, parser):
    try:
        tokens = word_tokenize(ilocano_sentence.lower())  # Tokenize sentence
        pos_tags = []
        # Get POS tags from the lexicon (add check for missing lexicon entries)
        for token in tokens:
            entry = lexicon.lookup(token)
            if entry and 'pos' in entry:
                pos_tags.append(entry['pos'][0])
            else:
                pos_tags.append('NN')  # Default POS tag (Noun) if not found
        trees = parser.parse(pos_tags)

        for tree in trees:
            transformed_tree = transform_tree(tree)
            english_sentence = get_english_sentence(transformed_tree, pos_tags, tokens, lexicon)
            return english_sentence
        return "CANNOT TRANSLATE"
    except Exception as e:
        return f"Translate Exception: {e}"

if __name__ == "__main__":
    ilocano_lex = IlocanoLexicon()
    grammar = IlocanoGrammar()
    parser = grammar.lookup_grammar_parser()

    ilocano_sentences = [
        "Agtaray ti aso",
        "Agkanta isuna",
        "Agbasa kami iti libro",
        "Agsangit ti pusa",
        "Agsurat ak iti diyaryo",
        "Aginana isuna",
        "Awan aso ditoy",
        "Naimbag nga aldaw",
        "Naimbag nga bigat",
        "Naimbag nga rabii",
        "Naimbag nga malem",
        "Dagiti agkakabsat ket agtrabtrabaho iti ili",
        "Agbasa kami ti libro",
        "Mangted isuna iti danum",
        "Agsursurat ak iti diyaryo",
        "Mangted ak iti bayabas",
        "Agbasa isuna iti ammo",
        "Agala ti lalaki iti danum",
        "Agtaray ti aso dagos",
        "Agtrabtrabaho kami ditoy",
        "Agbasa kami agingga alas dies",
        "ti balay ket dakkel",
        "Isuna ket nalaing",
        "Ti balay ket bassit",
        "Ti aso ket dakkel",
        "Ti danum ket nalamiis",
        "Kami ket agtrabtrabho",
        "Ti lalaki ket abogado",
        "Isuna ket agbasbasa",
        "Ti ubing ket naragsak",
        "Ti abogado ket dakes",
        "Isuna gumatang iti saba",
        "Ti dakkel nga balay ket napintas",
        "Ti bassit nga ubing ket naragsak",
        "Ti nangina nga libro ket narugit",
        "Agtaray kanayon ti ubing",
        "Agdigos metten ti lalaki",
        "Napan idiay tiendaan ita",
        "Agsangit unay ti balasang",
        "Agbasa isuna ti libro",
        "Ti pusa ket bassit",
        "Agtrabaho kami idiay balay",
        "Agkanta kayo iti bigat",
        "Nalaing ti abogado",
        "Agsursurat ak iti libro",
        "Aginana isuna iti aldaw",
        "Dakayo ket adda iti balay",
        "Ti dalan ket napigsa",
        "Daldalusan iti balay",
        "Adda ti biyahe itatta",
        "Ti datar ket nalinis",
        "Daytoy ket ti daya",
        "Dies dagiti maysa libro",
        "Dinalusan ti kuarto",
        "Ti kuarto ko ket naisagana",
        "Pimmanaw ti mangngalap",
        "Ti lames ket napigsa",
        "Kayat ko latta isuna",
        "Linambong ti gulay",
        "Makabannog ti trabaho",
        "Masapul ti makan",
        "Masapul nga agtrabaho",
        "Naladingit ti panagbiag ko",
        "Napuskol ti libro",
        "Narangrang ti aldaw",
        "Padi ti napan",
        "Agsakit ti ulok",
        "Pinidua ti trabaho",
        "Awan ti ginatang ko idiay ili",
        "Agsangit diay ubing",
        "Diay ubing agsangit",
        "Napintas ti balay ti balasang",
        "Nakakita isuna ken Marya",
        "Pumintas kanto met laeng",
        "Siak ti agawid",
        "Ubing ti nagsangit",
        "Diay aso ket nagtaul",
        "Nagtataray dagiti ubbing",
        "Basaen na ta libro",
        "Kitaen na ta ubing",
        "Kinatungtung na diay balasang",
        "Maipattug dayta danum",
        "Agtudo manen",
        "Nagsangit diay ubing idiay balay mi",
        "Naanus diay baket",
        "Kanayon ti panagtaray",
        "Narigat ti matay",
        "Narigat ti sadut ti anak na",
        "Nalamiis ditoy",
        "Kayat diay padi ti umay ditoy",
        "Kayat na ti gumatang iti balay",
        "Agsakitak sa",
        "Agsakit ti ulok",
        "Agtaray ti aso idiay dalan",
        "Agsakit ti tiyan ko",
        "Masapul ko ti doktor",
        "Mapanak idiay balay yo",
        "Mapanak pay",
        "Innak pay",
        "Agawid ak"

    ]

    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")

    print(len(ilocano_sentences))