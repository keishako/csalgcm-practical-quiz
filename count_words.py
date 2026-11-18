# word must appear at least 2 times to be kept
MIN_COUNT = 2
# word must have at least 2 letters to be kept
MIN_LEN = 2

def count_words(words, min_count=MIN_COUNT, min_len=MIN_LEN):
    # count every word using a dictionary (hashmap)
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1   # if seen before, increment 1
        else:
            counts[word] = 1    # if first time seeing this word, = 1

    stored = {}

    # keep words that appear at least min_count times and at least min_len letters
    for word, count in counts.items():
        if count >= min_count and len(word) >= min_len:
            stored[word] = count
    return stored
