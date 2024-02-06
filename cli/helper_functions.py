from proverbs_dictionary import proverbs_dict as proverbs

# Counts how many words does the input share with each proverb
def findProverb(proverb, proverbs):
    max_shared_count = 0 # To count the words
    language = "" # if its Eng, ... ?
    max_shared_combination = 0 #1st list, 2nd... ?

    for backup_list_name, proverbs_combinations in proverbs.items():
        for i, combination in enumerate(proverbs_combinations):
            shared_words = set(proverb) & set(combination)
            shared_count = len(shared_words)

            if shared_count > max_shared_count:
                max_shared_count = shared_count
                language = backup_list_name
                max_shared_combination = i

    return language, max_shared_combination

# Check the users input if it has any special charaters or numbers:
def checkSPandNmb(proverb):
    for char in proverb:
        if(not char.isalnum() and char not in [' ', ','] ):
            return False
    return True

# Check if the entered Proverb is correct:
# Not messing a word or some, not putting one before the other...
def proverbWordsCheking(proverb, proverb_found):
    # Messing Words:
    if(len(proverb) != len(proverb_found)):
        return False
    i = 0
    while i < len(proverb_found):
        if(proverb[i] != proverb_found[i]):
            return False
        i += 1
    
    return True

# Get the equivalent:
def equivalentProverbs(langage, index_list, proverbs):
    equivalents = {}
    for key_dic in proverbs:
        if key_dic != langage:
            equivalent_string = ' '.join(proverbs[key_dic][index_list])
            equivalents[key_dic] = equivalent_string
    return equivalents




