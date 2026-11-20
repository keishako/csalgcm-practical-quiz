import calamancy

with open('dataset/text_files/output_file_50.txt', 'r', encoding='utf-8') as file:
            lines = file.read()

nlp = calamancy.load("tl_calamancy_md")  # loads the latest version
doc = nlp(lines)
print([(ent.text, ent.label_) for ent in doc.ents])