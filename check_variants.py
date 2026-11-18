from find_difference import find_differences

ALLOWED_SWAPS = {
    ("ch", "ts"),
    ("e", "i"),
    ("o", "u"),
    ("uw", "w"),
    ("iy", "y"),
    ("d", "r"),
    ("c", "k"),
    ("v", "b"),
    ("f", "p"),
    # add more when dataset is released
}

# assuming that max num of places where 2 words can be different
MAX_DIFF = 1

# check if this pair is a real spelling variant
def is_valid_variant(word1, word2, dictionary):
    # find which letters are different
    diffs = find_differences(word1, word2)

    # reject if cant compare/ no difference (same word) / more than MAX_DIFF
    if diffs == None or len(diffs) == 0 or len(diffs) > MAX_DIFF: return False, None

    # reject if difference is not allowed spelling change
    for (a,b) in diffs:
        if (a, b) not in ALLOWED_SWAPS and (b, a) not in ALLOWED_SWAPS: return False, None

    # reject if both words are different words in dictionary
    if word1 in dictionary and word2 in dictionary: return False, None

    # spelling variant
    return True, diffs

# greedy algo
# pairing each word with the most common spelling (main word)
def make_pairs(group, counts, dictionary):
    # sort by count, most common first 
    group.sort(key = lambda w: counts[w], reverse = True)

    pairs = []

    # start 2nd word (other word), most common 1st word(main_word)
    for i in range(1, len(group)):
        other_word = group[i]

        for main_word in group[:i]:
            ok, diffs = is_valid_variant(main_word, other_word, dictionary)

            if ok: 
                pairs.append((main_word, other_word, diffs))
                break

    return pairs 