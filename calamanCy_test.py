import calamancy

nlp = calamancy.load("tl_calamancy_md")  # loads the latest version

clean_words = []        # dataset without proper nouns
proper_noun_words = []  # proper noun words that are removed (for checking purposes)

# dataset/text_files/output_file_50.txt
with open('output_file_150.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

for doc in nlp.pipe(lines, batch_size=50):
    for token in doc:
        is_proper_name = bool(token.ent_type_)

        is_capital_mid_sentence = token.text[:1].isupper() and not token.is_sent_start

        if is_proper_name or is_capital_mid_sentence:
            proper_noun_words.append(token.text)
        elif token.is_alpha:
            clean_words.append(token.text.lower())

    print([(ent.text, ent.label_) for ent in doc.ents])

with open("clean_output_file_50.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(clean_words))

with open("proper_noun_output_file_50.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(proper_noun_words))
