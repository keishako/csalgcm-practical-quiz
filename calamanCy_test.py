import calamancy

nlp = calamancy.load("tl_calamancy_md")  # loads the latest version

clean_words = []        # dataset without proper nouns
proper_noun_words = []  # proper noun words that are removed (for checking purposes)

# dataset/text_files/output_file_50.txt
with open('output_file_50.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

for doc in nlp.pipe(lines, batch_size=50):
    for token in doc:
        if token.ent_type_:         # if proper noun, remove then put proper_noun_words
            proper_noun_words.append(token.text)
        elif token.is_alpha:          # clean word = kept
            clean_words.append(token.text.lower())
    print([(ent.text, ent.label_) for ent in doc.ents])

with open("clean_output_file_50.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(clean_words))

with open("proper_noun_output_file_50.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(proper_noun_words))
