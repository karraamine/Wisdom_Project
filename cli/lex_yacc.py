import ply.lex as lex
import ply.yacc as yacc
from proverbs_dictionary import proverbs_dict as proverbs
from helper_functions import *

result = {}

def action_semantique(p):
    proverbsEnglishList = proverbs['English']
    
    if p[1] == 'many':
        if p[2] == 'hands'and p[3] == 'make' and p[4] == 'light' and p[5] == 'work':
            print("Correct Proverb.")
            return True, proverbsEnglishList[0]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[0]
        
    elif p[1] == 'strike':
        if p[2] == 'while' and p[3] == 'the' and p[4] == 'iron' and p[5] == 'is' and p[6] == 'hot':
            print("Correct Proverb.")
            return True, proverbsEnglishList[1]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[1]
    elif p[1] == 'honesty':
        if p[2] == 'is'and p[3] == 'the' and p[4] == 'best' and p[5] == 'policy':
            print("Correct Proverb.")
            return True, proverbsEnglishList[2]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[2]
    elif p[1] == 'you':
        if p[2] == 'only'and p[3] == 'fail' and p[4] == 'when' and p[5] == 'you' and p[6] == 'stop' and p[7] == 'trying':
            print("Correct Proverb.")
            return True, proverbsEnglishList[3]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[3]
    elif p[1] == "don't":
        if p[2] == 'bite'and p[3] == 'the' and p[4] == 'hand' and p[5] == 'that' and p[6] == 'feeds' and p[7] == 'you':
            print("Correct Proverb.")
            return True, proverbsEnglishList[4]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[4]
    elif p[1] == "birds":
        if p[2] == 'of'and p[3] == 'a' and p[4] == 'feather' and p[5] == 'flock' and p[6] == 'together':
            print("Correct Proverb.")
            return True, proverbsEnglishList[5]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[5]
    elif p[1] == "they":
        if p[2] == 'hate'and p[3] == 'us' and p[4] == 'cause' and p[5] == 'they' and p[6] == "ain't" and p[7] == "us":
            print("Correct Proverb.")
            return True, proverbsEnglishList[6]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[6]
    elif p[1] == "physician":
        if p[2] == 'heal'and p[3] == 'thyself':
            print("Correct Proverb.")
            return True, proverbsEnglishList[7]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[7]
    elif p[1] == "early":
        if p[2] == 'bird'and p[3] == 'catches' and p[4] == 'the' and p[5] == 'worm':
            print("Correct Proverb.")
            return True, proverbsEnglishList[8]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[8]
    elif p[1] == "empty":
        if p[2] == 'vessels'and p[3] == 'make' and p[4] == 'much' and p[5] == 'noise':
            print("Correct Proverb.")
            return True, proverbsEnglishList[9]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[9]
    elif p[1] == "hard":
        if p[2] == 'work'and p[3] == 'brings' and p[4] == 'sweet' and p[5] == 'fruit':
            print("Correct Proverb.")
            return True, proverbsEnglishList[10]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[10]
    elif p[1] == "learn":
        if p[2] == 'to'and p[3] == 'walk' and p[4] == 'before' and p[5] == 'you' and p[6] == "run":
            print("Correct Proverb.")
            return True, proverbsEnglishList[11]
        else:
            print("Wrong Proverb!")
            return False, proverbsEnglishList[11]
        
    # ------------- DARIJA --------------
    proverbsDarijaList = proverbs['Darija']
    
    if p[1] == 'yedd':
        if p[2] == 'waheda'and p[3] == 'makatessfe9ch':
            print("Correct Proverb.")
            return True, proverbsDarijaList[0]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[0]
        
    elif p[1] == 'dreb':
        if p[2] == 'lhdid' and p[3] == 'maheddo' and p[4] == 'skhon':
            print("Correct Proverb.")
            return True, proverbsDarijaList[1]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[1]
    elif p[1] == '9asseh':
        if p[2] == 'hessan' and p[3] == 'mn' and p[4] == 'lkeddab':
            print("Correct Proverb.")
            return True, proverbsDarijaList[2]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[2]
    elif p[1] == 'libgha':
        if p[2] == 'la3ssel' and p[3] == 'yessbr' and p[4] == 'l9riss' and p[5] == 'nhell':
            print("Correct Proverb.")
            return True, proverbsDarijaList[3]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[3]
    elif p[1] == "madir":
        if p[2] == 'khir' and p[3] == 'mayterra' and p[4] == 'bas':
            print("Correct Proverb.")
            return True, proverbsDarijaList[4]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[4]
    elif p[1] == "m3amen":
        if p[2] == 'chetk' and p[3] == 'm3amen' and p[4] == 'chebhtk':
            print("Correct Proverb.")
            return True, proverbsDarijaList[5]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[5]
    elif p[1] == "mahedek":
        if p[2] == 'hadini' and p[3] == 'u' and p[4] == 'rebbi' and p[5] == '3attini':
            print("Correct Proverb.")
            return True, proverbsDarijaList[6]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[6]
    elif p[1] == "kon":
        if p[2] == 'kan' and p[3] == 'lkhoukh' and p[4]=='yedawi' and p[5]=='kon' and p[6]=='dawa' and p[7]=='rasso':
            print("Correct Proverb.")
            return True, proverbsDarijaList[7]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[7]
    elif p[1] == "lfya9":
        if p[2] == "bekri" and p[3] == "b" and p[4]=="dheb" and p[5]=="macheri":
            print("Correct Proverb.")
            return True, proverbsDarijaList[8]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[8]
    elif p[1] == "lkelb":
        if p[2] == "li" and p[3] == "kaynbh" and p[4]=="ga3" and p[5]=="makay" and p[6]=="3ad":
            print("Correct Proverb.")
            return True, proverbsDarijaList[9]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[9]
    elif p[1] == "de9a":
        if p[2] == "de9a" and p[3] == "yahml" and p[4]=="lwad":
            print("Correct Proverb.")
            return True, proverbsDarijaList[11]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsDarijaList[11]
    # ------ Français --------- # --- Italiano -----
    proverbsFrançaisList = proverbs['Français']

    if p[1] == 'plusieurs':
        if p[2] == 'mains' and p[3] == 'rendent' and p[4] == 'le' and p[5] == 'travail' and p[6] == 'léger':
            print("Correct Proverb.")
            return True, proverbsFrançaisList[0]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[0]
    if p[1] == "il":
        if p[2] == "faut" and p[3] == "battre" and p[4] == 'le' and p[5] == "fer" and p[6] == "pendant" and p[7] == "qu'il" and p[8] == "est" and p[9] == "chaud":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[1]
        elif p[2] == "ne":
            if p[3] == "faut" and p[4] == "pas" and p[5] == "jeter" and p[6] == "le" and p[7] == "manche" and p[8] == "après" and p[9] == "la" and p[10] == "cognée":
                print("Correct Proverb.")
                return True, proverbsFrançaisList[4]
            else:
                print("!!! Error was detected !!!")
                print("You Respected the format of the sentence, but not the sequence of words.")
                return False, proverbsFrançaisList[4]
        elif p[2] == 'frutto':
            if p[3] == 'del' and p[4] == 'sudore' and p[5] == 'è' and p[6] == 'più' and p[7] == 'dolce':
                print("Correct Proverb.")
                return True, proverbsItalianoList[10]
            else:
                print("Wrong Proverb!")
                return False, proverbsItalianoList[10]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[1]
    if p[1] == "l'honnêteté":
        if p[2] == "est" and p[3] == "la" and p[4] == "meilleure" and p[5] == "politique":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[2]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[2]
    if p[1] == "le":
        if p[2] == "chemin":
            if p[3] == "de" and p[4] == "la" and p[5] == "réussite" and p[6] == "est" and p[7] == "pavé" and p[8] == "d'échecs":
                print("Correct Proverb.")
                return True, proverbsFrançaisList[3]
            else:
                print("!!! Error was detected !!!")
                print("You Respected the format of the sentence, but not the sequence of words.")
                return False, proverbsFrançaisList[3]
        elif p[2] == "monde":
            if p[3] == "appartient" and p[4] == "à" and p[5] == "ceux" and p[6] == "qui" and p[7] == "se" and p[8] == "lèvent" and p[9] == "tôt":
                print("Correct Proverb.")
                return True, proverbsFrançaisList[7]
            else:
                print("!!! Error was detected !!!")
                print("You Respected the format of the sentence, but not the sequence of words.")
                return False, proverbsFrançaisList[7]
    if p[1] == "qui":
        if p[2] == "se" and p[3] == "ressemble" and p[4] == "s'assemble":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[5]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[5]
    if p[1] == "l'envie":
        if p[2] == "est" and p[3] == "un" and p[4] == "serpent" and p[5] == "qui" and p[6] == "se" and p[7] == "mord" and p[8] == "la" and p[9] == "queue":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[6]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[6]
    if p[1] == "les":
        if p[2] == "cordonniers" and p[3] == "sont" and p[4] == "toujours" and p[5] == "les" and p[6] == "plus" and p[7] == "mal" and p[8] == "chaussés":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[7]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[7]
        
    if p[1] == "petit":
        if p[2] == "à" and p[3] == "petit" and p[4] == "l'oiseau" and p[5] == "fait" and p[6] == "son" and p[7] == "nid":
            print("Correct Proverb.")
            return True, proverbsFrançaisList[11]
        else:
            print("!!! Error was detected !!!")
            print("You Respected the format of the sentence, but not the sequence of words.")
            return False, proverbsFrançaisList[11]
        
    # ------- Espaniol -----------
    proverbsEspaniolList = proverbs['Espaniol']
    if p[1] == 'muchas':
        if p[2] == 'manos' and p[3] == 'hacen' and p[4] == 'el' and p[5] == 'trabajo' and p[6] == 'ligero':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[0]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[0]
    elif p[1] == 'hierro':
        if p[2] == 'candente' and p[3] == 'batirlo' and p[4] == 'o' and p[5] == 'perderlo':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[1]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[1]
    elif p[1] == 'la':
        if p[2] == 'envidia':
            if p[3] == 'no' and p[4] == 'engorda':
                print("Correct Proverb.")
                return True, proverbsEspaniolList[6]
            else:
                print("Wrong Proverb!")
                return False, proverbsEspaniolList[6]
        elif p[2] == 'honradez':
            if p[3] == 'es' and p[4] == 'la' and p[5] == 'mejor' and p[6] == 'riqueza':
                print("Correct Proverb.")
                return True, proverbsEspaniolList[2]
            else:
                print("Wrong Proverb!")
                return False, proverbsEspaniolList[2]
    elif p[1] == 'nunca':
        if p[2] == 'es' and p[3] == 'tarde' and p[4] == 'si' and p[5] == 'la' and p[6] == 'dicha' and p[7] == 'es' and p[8] == 'buena':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[3]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[3]
    elif p[1] == 'no':
        if  p[2] == 'se':
            if p[3] == 'empieza' and p[4] == 'la' and p[5] == 'casa' and p[6] == 'por' and p[7] == 'el' and p[8] == 'tejado':
                print("Correct Proverb.")
                return True, proverbsEspaniolList[11]
            else:
                print("Wrong Proverb!")
                return False, proverbsEspaniolList[11]
        elif p[2] == 'muerdas':
            if p[3] == 'la' and p[4] == 'mano' and p[5] == 'qué' and p[6] == 'te' and p[7] == 'da' and p[8] == 'de' and p[9] == 'comer':
                print("Correct Proverb.")
                return True, proverbsEspaniolList[4]
            else:
                print("Wrong Proverb!")
                return False, proverbsEspaniolList[4]
    elif p[1] == 'dios':
        if p[2] == 'los' and p[3] == 'cria' and p[4] == 'y' and p[5] == 'ellos' and p[6] == 'se' and p[7] == 'juntan':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[5]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[5]
    elif p[1] == 'médico':
        if p[2] == 'curate' and p[3] == 'a' and p[4] == 'ti' and p[5] == 'mismo':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[7]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[7] 
    elif p[1] == 'al':
        if p[2] == 'que' and p[3] == 'madruga' and p[4] == 'dios' and p[5] == 'le' and p[6] == 'ayuda':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[8]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[8]
    elif p[1] == 'perro': 
        if p[2] == 'que' and p[3] == 'ladra' and p[4] == 'no' and p[5] == 'muerde':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[9]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[9]
    elif p[1] == 'el':
        if p[2] == 'fruto' and p[3] == 'del' and p[4] == 'trabajo' and p[5] == 'es' and p[6] == 'dulce':
            print("Correct Proverb.")
            return True, proverbsEspaniolList[10]
        else:
            print("Wrong Proverb!")
            return False, proverbsEspaniolList[10]
    
    # ------- Italiano -----------
    proverbsItalianoList = proverbs['Italiano']
    if p[1] == "l'unione":
        if p[2] == "fa" and p[3] == 'la' and p[4] == 'forza':
            print("Correct Proverb.")
            return True, proverbsItalianoList[0]
        else:
            print("Wrong Proverb!")
            return False, proverbsItalianoList[0]
    elif p[1] == 'la':
        if p[2] == 'sincerità':
            if p[3] == 'è' and p[4] == 'sempre' and p[5] == 'premiata':
                print("Correct Proverb.")
                return True, proverbsItalianoList[2]
            else:
                print("Wrong Proverb!")
                return False, proverbsItalianoList[2]
        elif p[2] == 'fretta':
            if p[3] == 'è' and p[4] == 'nemica' and p[5] == 'della' and p[6] == 'perfezione':
                print("Correct Proverb.")
                return True, proverbsItalianoList[11]
            else:
                print("Wrong Proverb!")
                return False, proverbsItalianoList[11]
    elif p[1] == 'chi':
        if p[2] == 'non':
            if p[3] == 'tenta':
                if p[4] == 'non' and p[5] == 'sfonda':
                    print("Correct Proverb.")
                    return True, proverbsItalianoList[3]
                else:
                    print("Wrong Proverb!")
                    return False, proverbsItalianoList[3]
            elif p[3] == 'ci':
                if p[4] == 'apprezza' and p[5] == 'non' and p[6] == 'ci' and p[7] == 'merita':
                    print("Correct Proverb.")
                    return True, proverbsItalianoList[6]
                else:
                    print("Wrong Proverb!")
                    return False, proverbsItalianoList[6]
        elif p[2] =='si':
            if p[3] == 'somiglia' and p[4] == 'si' and p[5] == 'piglia':
                print("Correct Proverb.")
                return True, proverbsItalianoList[5]
            else:
                print("Wrong Proverb!")
                return False, proverbsItalianoList[5]
        elif p[2] == 'dorme':
            if p[3] == 'non' and p[4] == 'piglia' and p[5] == 'pesci':
                print("Correct Proverb.")
                return True, proverbsItalianoList[8]
            else:
                print("Wrong Proverb!")
                return False, proverbsItalianoList[8]
    elif p[1] == 'predica':
        if p[2] == 'bene' and p[3] == 'e' and p[4] == 'razzola' and p[5] == 'male':
            print("Correct Proverb.")
            return True, proverbsItalianoList[7]
        else:
            print("Wrong Proverb!")
            return False, proverbsItalianoList[7]
    elif p[1] == 'can':
        if p[2] == 'che' and p[3] == 'abbaia' and p[4] == 'non' and p[5] == 'morde':
            print("Correct Proverb.")
            return True, proverbsItalianoList[9]
        else:
            print("Wrong Proverb!")
            return False, proverbsItalianoList[9]
        
# Define the tokens
tokens = ['VERB', 'ADJECTIVE', 'NOUN', 'CONJUNCTION', 'ARTICAL', 'PRONOUN', 
          'ADVERB', 'GERUND', 'CONTRUDICTION', 'PREPOSITION']

t_VERB = r'(fa|è|tenta|somiglia|sfonda|piglia|apprezza|merita|predica|razzola|dorme|piglia|abbaia|morde|hacen|batirlo|perderlo|es|muerdas|da|comer|cria|juntan|engorda|curate|madruga|ayuda|ladra|muerde|empieza|fait|mangeras|aboient|passe|appartient|lèvent|sont|ressemble|s\'assemble|mord|jeter|faut|battre|est|rendent|pavé|3ad|makatessfe9ch|dreb|yessbr|madir|mayterra|chetk|chebhtk|libgha|hadini|3attini|yedawi|dawa|kan|kaynbh|yahml|make|strike|is|fail|stop|bite|feeds|flock|hate|heal|catches|brings|learn|walk|run)'
t_ADJECTIVE = r"(premiata|bene|male|dolce|nemica|muchas|ligero|candente|mejor|tarde|buena|dulce|son|petit|ton|chaussés|d'échecs|honnêteté|meilleure|chaud|plusieurs|léger|waheda|skhon|9asseh|hessan|lkeddab|bekri|macheri|many|light|hot|best|early|empty|hard|sweet|much)"
t_NOUN = r'(l\'unione|forza|sincerità|pesci|can|frutto|sudore|fretta|perfezione|manos|trabajo|hierro|honradez|riqueza|dicha|mano|dios|envidia|médico|perro|fruto|casa|tejado|l\'oiseau|nid|sueur|front|pain|chiens|caravane|monde|cordonniers|envie|serpent|queue|manche|cognée|chemin|réussite|échecs|politique|mains|travail|yedd|lhdid|la3ssel|lkriss|nhell|khir|bas|rebbi|lkhoukh|lfya9|dheb|lkelb|de9a|lwad|hands|work|iron|honesty|policy|hand|birds|feather|physician|bird|worm|vessels|noise|fruit)'
t_CONJUNCTION = r'(e|che|o|si|y|que|pendant|maheddo|mahedek|o|kon|li|makay|while|when|that|cause)'
t_ARTICAL = r'(il|el|del|les|un|la|le|the)'
t_PRONOUN = r'(chi|ci|te|los|ellos|ti|mismo|c\'est|qué|tu|ceux|qui|se|qu\'il|rasso|they|you|us|thyself)'
t_ADVERB = r'(sempre|non|più|nunca|no|tôt|toujours|plus|mal|ne|pas|only|together)'
t_GERUND = r'(trying)'
t_CONTRUDICTION = r"(don't|ain't|ga3)"
t_PREPOSITION = r'(della|a|por|à|après|de|mn|m3amen|b|of|to|before)'


# Define the ignore rule for spaces
t_ignore = " \t'"

def t_error(t):
   print("Illegal character:", t.value[0], "at index", t.lexpos)
   t.lexer.skip(1)  # Skip the invalid character

# Define the grammar rules
def p_sentence(p):
    # Systaxique
    '''sentence : ADJECTIVE NOUN VERB ADJECTIVE NOUN
                | VERB CONJUNCTION ARTICAL NOUN VERB ADJECTIVE
                | NOUN VERB ARTICAL ADJECTIVE NOUN
                | PRONOUN ADVERB VERB CONJUNCTION PRONOUN VERB GERUND
                | CONTRUDICTION VERB ARTICAL NOUN CONJUNCTION VERB PRONOUN
                | NOUN PREPOSITION PREPOSITION NOUN VERB ADVERB
                | PRONOUN VERB PRONOUN CONJUNCTION PRONOUN CONTRUDICTION PRONOUN
                | NOUN VERB PRONOUN
                | VERB PREPOSITION VERB PREPOSITION PRONOUN VERB
                |  NOUN ADJECTIVE VERB
                | VERB NOUN CONJUNCTION ADJECTIVE
                | VERB NOUN VERB NOUN NOUN
                | VERB NOUN VERB NOUN
                | PREPOSITION VERB PREPOSITION VERB
                | ADJECTIVE ADJECTIVE PREPOSITION ADJECTIVE
                | CONJUNCTION VERB CONJUNCTION NOUN VERB
                | CONJUNCTION VERB NOUN VERB CONJUNCTION VERB PRONOUN
                | NOUN NOUN VERB NOUN
                | NOUN CONJUNCTION VERB CONTRUDICTION CONJUNCTION VERB
                | NOUN ADJECTIVE PREPOSITION NOUN ADJECTIVE
                | ADJECTIVE NOUN VERB ARTICAL NOUN ADJECTIVE
                | NOUN ADJECTIVE VERB CONJUNCTION VERB
                | ARTICAL NOUN VERB ARTICAL ADJECTIVE NOUN
                | ADVERB VERB ADJECTIVE CONJUNCTION ARTICAL NOUN VERB ADJECTIVE
                | ADVERB VERB ARTICAL NOUN PRONOUN PRONOUN VERB PREPOSITION VERB
                | NOUN PRONOUN VERB CONJUNCTION PRONOUN PRONOUN VERB
                | ARTICAL NOUN ADVERB VERB
                | NOUN VERB PREPOSITION PRONOUN PRONOUN
                | ARTICAL PRONOUN VERB NOUN ARTICAL VERB
                | NOUN PRONOUN VERB ADVERB VERB
                | ARTICAL NOUN ARTICAL NOUN VERB ADJECTIVE
                | ADVERB PRONOUN VERB ARTICAL NOUN PREPOSITION ARTICAL NOUN
                | NOUN VERB ARTICAL NOUN
                | ARTICAL NOUN VERB ADVERB ADJECTIVE
                | PRONOUN ADVERB VERB ADVERB VERB
                | PRONOUN CONJUNCTION VERB CONJUNCTION VERB
                | PRONOUN ADVERB PRONOUN VERB ADVERB PRONOUN VERB 
                | VERB ADJECTIVE CONJUNCTION VERB ADJECTIVE
                | PRONOUN VERB ADVERB VERB NOUN
                | NOUN CONJUNCTION VERB ADVERB VERB 
                | ARTICAL NOUN ARTICAL NOUN VERB ADVERB ADJECTIVE
                | ARTICAL NOUN VERB ADJECTIVE PREPOSITION NOUN'''
    
    # Why use it here
    # Say the user entered: 'many hands fail hot honesty' intead of 'many hands make light work'
    # It repects the fromat of the sentence, but not the proverb's sequence of words.
    # Sémantique
    print("Action Sematique")
    situation, correct_proverb = action_semantique(p)
    result['situation'] = situation
    

    langage, index_list = findProverb(correct_proverb, proverbs)
    result['origin'] = {'langage':langage, 'correct_proverb': ' '.join(correct_proverb)}
    

    # Get equivalents:
    if situation:
        equivalents = equivalentProverbs(langage, index_list, proverbs)
        print("Equivalents of this proverb in other langages: ")
        result["equivalents"] = {}
        for key_dic, equi in equivalents.items():
            print(f"{key_dic}: {equi}")
            result["equivalents"][key_dic] = equi
            
            
    else:
        print("Did you mean: ", ' '.join(correct_proverb))
        print("Try Again")

    


def p_error(p):
    action_semantique(p)

# Build the lexer
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()

# Function to check if a sentence is correct or not
def check_sentence(sentence):
    lexResult = parser.parse(sentence)
    return lexResult

# Example usage
def compilation():
    user_input = input("Enter a sentence: ").lower()
    try:
        lexResult = check_sentence(user_input)
    except:
        proverb = user_input.split(' ')
        langage, index_list = findProverb(proverb, proverbs)
        proverb_found = proverbs[langage][index_list]
        if proverbWordsCheking(user_input.split(' '), proverb_found):
            result["situation"] = True
            proverb = user_input.split(' ')
            proverb_string = ' '.join(proverb_found)
            result["origin"] = {"langage":langage, "correct_proverb": proverb_string}
            equivalents = equivalentProverbs(langage, index_list, proverbs)
            print("Equivalents of this proverb in other langages: ")
            result["equivalents"] = {}
            for key_dic, equi in equivalents.items():
                print(f"{key_dic}: {equi}")
                result["equivalents"][key_dic] = equi
        else:
            result["situation"] = False
            if(checkSPandNmb(user_input)):
                try:
                    proverb_string = ' '.join(proverb_found)
                    result["origin"] = {"langage":langage, "correct_proverb": proverb_string}
                    if(not proverbWordsCheking(proverb, proverb_found)):
                        print("!!! Error was detected !!!")
                        print(f"Did you mean this: {proverb_string}")
                except KeyError:
                    print("Not Found in our data!")
    print("result: ", result)
    print("\n--------------------------------------\n")
    return result

while True:
    compilation()


