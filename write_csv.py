import csv

def write_csv(pairs, counts, path="variants.csv"):
    rows = []

    for main_word, other_word, diffs in pairs:
        # put 2 words in alphabetical order
        word1, word2 = sorted([main_word, other_word])

        # if sorting swapped the order, flip difference e.g. (u, o) -> (o, u)
        if word1 != main_word:
            diffs = [(b, a) for a, b in diffs]

        # split into 2 letters e.g. (o, u) -> a = o, b = u
        a, b = diffs[0]
        diff_text = f"{a} vs. {b}"      # ex: "o vs. u"

        rows.append([word1, word2, counts[word1], counts[word2], diff_text])

    # write file
    with open(path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word1', 'word2', 'word1_count', 'word2_count', 'character_difference'])
        writer.writerows(rows)

    return len(rows)