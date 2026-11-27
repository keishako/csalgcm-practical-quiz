import csv

# word must appear at least 2 times to be kept
MIN_COUNT = 10
# word must have at least 2 letters to be kept
MIN_LEN = 3

file_path = "dataset/WHOLE_calamanCy-result/combined_clean_output.txt"
# file_path = "clean_output_file_50.txt" # for testing

with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read()

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

if __name__ == "__main__":
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    tokens = text.split()
    filtered_counts = count_words(tokens)

    with open('results/csvfiles/count_words.csv', 'w', newline="", encoding='utf-8') as counted_file:
        writer = csv.writer(counted_file)
        writer.writerow(["word", "count"])
        # sort second part (count)
        # descending: put reverse=True
        for key, value in sorted(filtered_counts.items(), key=lambda item: item[1]):
            writer.writerow([key, value])

    print("count_words.csv is in the files")

