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
            english_words.append(ilocano_word)
    return " ".join(english_words)

def translate_to_english(ilocano_sentence, lexicon, parser):
    try:
        tokens = word_tokenize(ilocano_sentence.lower())
        pos_tags = [lexicon.lookup(token)['pos'][0] if lexicon.lookup(token) and 'pos' in lexicon.lookup(token) else token for token in tokens]
        trees = parser.parse(pos_tags)
        for tree in trees:
            transformed_tree = transform_tree(tree)
            english_sentence = get_english_sentence(transformed_tree, pos_tags, tokens, lexicon)
            return english_sentence
        return "CANNOT TRANSLATE"
    except Exception as e:
        return f"error nga kulet: {e}"

if __name__ == "__main__":
    ilocano_lex = IlocanoLexicon()
    grammar = IlocanoGrammar()
    parser = grammar.lookup_grammar_parser()

    ilocano_sentences = [
        "adda tao idiay balay",
        "adda ti tao idiay balay",
        "awan tao idiay balay",
        "awan ti tao idiay balay",
        "adda idiay balay diay ubing",
        "diay ubing ti adda idiay balay",
        "ubing ti adda idiay balay",
        "awan ti ginatang ko idiay ili",
        "agdigdigos",
        "diay balasang ti napintas ti balay na",
        "kaaduen na ti mangan",
        "sapaen na ti umay ditoy",
        "partakan na ti magna",
        "piduaen na ti mangan",
        "pitloen na nga digusen diay ubing",
        "namindua da nga nangan",
        "pinidua da ti nangan",
        "agsangit diay ubing",
        "diay ubing ti agsangit",
        "ubing ti agsangit",
        "diay ubing agsangit",
        "diay ubing ket agsangit",
        "gatangen diay ubing diay mangga",
        "gumatang iti mangga diay ubing",
        "diay ubing ti gumatang kadeydiay mangga",
        "isu ti nakakita ken marya",
        "isu ti nakakita ken ni marya",
        "isu ti nakakita kada marya",
        "pinuted na diay kawayan babaen iti buneng ko",
        "napan diay ubing idiay ili",
        "makisao diay baro idiay balasang",
        "nagsangit diay ubing gapo iti bisin",
        "nangan iti adu diay rawet",
        "nagna iti adayo diay ubing",
        "pumintas kanto met laeng",
        "umuli ka idiay balay",
        "mangan ti mangga diay ubing",
        "gumatang diay ubing ti mangga idiay ili para kadeydiay balasang",
        "isubli na deytoy idiay baket",
        "nakitungtung diay baro kadeydiay balasang",
        "nakisala diay baro iti tanggo kadeydiay balasang",
        "siak ti agawid",
        "ubing ti nagsangit",
        "diay aso ket nagtaul",
        "nagtungtung diay baro ken balasang",
        "nagkinnita diay baro ken balasang",
        "nagtataray dagiti ubbing",
        "basaen na ta libro",
        "pukisan na ta ubing",
        "isubli na talibro idiay titser",
        "mabasa na inton bigat ta libro nga ita",
        "dawatan na ti kuarta diay padi",
        "igatangan na ti mangga diay balasang",
        "pagputed na ti kawayan diay buneng ko",
        "kinatungtung na diay balasang",
        "malarya ti ipatay dayta ubing",
        "an-anayen dayta adigi",
        "matuduan dayta ubing",
        "malungsot dayta mangga",
        "maipattug dayta danum",
        "agtudo manen",
        "nagtudo ti yelo idi kalman",
        "yelo ti intudo na idi kalman",
        "rabii manen",
        "sumipngeten",
        "nagsangit diay ubing idi kalman",
        "nagsangit diay ubing idiay balay mi",
        "idi kalman ti panagsangit diay ubing",
        "idiay balay mi ti nagsangitan diay ubing",
        "ni pedro ka",
        "deytoy-ak",
        "siak deytoy",
        "rabiin",
        "naanus diay baket",
        "kanayon ti panagtaray na",
        "narigat ti matay",
        "narigat ti sadut ti anak na",
        "nalamiis ditoy",
        "tallo ti tao idiay balay",
        "sagsisingko dagita saba",
        "para kadeydiay balasang ta sabong",
        "nagpataray diay lalaki iti ubing",
        "nagpapataray diay lalaki iti ubing idiay lakay",
        "pagsalaen na diay balasang",
        "paulien na diay balasang",
        "pagpagatangen na diay lalaki iti asin",
        "ipapagatang na diay asin idiay lalaki",
        "agpaturog diay balasang iti ubing",
        "paturogen diay balasang diay ubing",
        "agpapaturog diay baket iti ubing idiay balasang",
        "ipapaturog diay baket diay ubing idiay balasang",
        "pagpaturogen diay baket diay balasang iti ubing",
        "nagpaluto diay baket iti innapoy idiay balasang",
        "paglutoen diay baket diay balasang iti innapoy",
        "ipaluto diay baket diay innapoy idiay balasang",
        "pagatangen na diay ubing iti asin",
        "ipagatangan na diay baket iti asin",
        "pagpaputed na diay buneng ko iti kawayan",
        "agpapagatang diay baket iti asin idiay ubing",
        "pagpagatangen diay baket diay balasang iti asin",
        "diay padi ti agpatudo inton bigat",
        "imbaga na nga mabisin ka",
        "baonen na diay balasang nga agdigos",
        "umay ka ditoy kuna na",
        "ti imbaga na mabisin ka",
        "nasayaat ta adda ka",
        "mabalin nga maturogak idiay",
        "ti damag ko ket dua ti anak mon",
        "ti bilin na ket daytoy",
        "nagtudo ken nagbagyo",
        "mangan ka no mabisin ka",
        "isu ti saan nga abugado",
        "saam nga napintas diay balay mo",
        "saam nga diay balay mo ti napintas",
        "saam ka nga napintas",
        "agdigdigosak",
        "mayat diay padi nga umay ka ditoy",
        "kayat diay padi ti umay ditoy",
        "kayat na ti gumatang ti balay",
        "balay ti kayat na nga gatangen"
    ]

    for sentence in ilocano_sentences:
        english_translation = translate_to_english(sentence, ilocano_lex, parser)
        print(f"Ilocano: {sentence}")
        print(f"English: {english_translation}\n")

    print(len(ilocano_sentences))