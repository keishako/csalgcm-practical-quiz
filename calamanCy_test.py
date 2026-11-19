import calamancy

nlp = calamancy.load("tl_calamancy_md")  # loads the latest version
doc = nlp("Ako si Juan de la Cruz")
print([(ent.text, ent.label_) for ent in doc.ents])