import pandas as pd
import csv
import unicodedata

filename = "results/csvfiles/count_words.csv"

# each rule: (old, new), order matters
KEY_RULES = [
    ("-", ""),
    ("'", ""),
    ("ch", "ts"),
    ("e", "i"),
    ("o", "u"),
    ("uw", "w"),
    ("iy", "y"),
    ("d", "r"),
    ("c", "k"),
    ("v", "b"),
    ("f", "p"),
    ("u", ""),
    ("i", ""),
]

# word into simplified version (replace old with new) using KEY_RULES
def make_key(word):
    key = word
    for old, new in KEY_RULES:
        key = key.replace(old, new)
    return key

# merge and merge sort by sorting list of (key, word) tuples alphabetically
def merge(left, right):
    result = []
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result

def merge_sort(items):
    if len(items) <= 1: return items        # base case
    mid = len(items) // 2                   # divide into half
    left = merge_sort(items[:mid])          # conquer left half
    right = merge_sort(items[mid:])         # conquer right half

    return merge(left, right)               # combine

# collect words that share the same key into groups, only 2 or more words are kept
def make_groups(counts):
    items = []

    for word in counts:
        items.append((make_key(word), word))

    sorted_items = merge_sort(items)

    groups = []     # finished group that are kept
    current = []    # group being filled
    prev_key = None

    for key, word in sorted_items:
        # same key as prev key then add to current group
        if key == prev_key: current.append(word)
        else:
            # if new key, current group is finished. keep if at least 2 words
            if len(current) >= 2:
                groups.append(current)
            # start new group with this word
            current = [word]
        # remember this key to compare next
        prev_key = key

    # check last group if no new key comes after it
    if len(current) >= 2:
        groups.append(current)

    return groups
    
if __name__ == "__main__":
    df = pd.read_csv(filename, usecols = [0], encoding="utf-8")

    words = []
    for raw in df.iloc[:, 0].dropna(): 
        cleaned = unicodedata.normalize("NFC", str(raw)).strip().lower() # normalizes accented letters
        if cleaned:
            words.append(cleaned)

    groups = make_groups(words)

    with open("results/csvfiles/grouped_words.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["group_id", "word"])

        for group_id, group in enumerate(groups, start=1):
            for word in group:
                writer.writerow([group_id, word])

        print("grouped_words.csv is in the files")

    