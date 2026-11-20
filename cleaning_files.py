import os
import re
import pandas as pd
import nltk

from nltk.corpus import stopwords 

dataset_path = r"dataset/text_files"

def load_corpus(folder):
    texts = []
    for file in os.listdir(folder):
        if file.endswith(".txt"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                texts.append(f.read())

    return texts

text_files = load_corpus(dataset_path)

print(f"Loaded {len(text_files)} files from text_files")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"https\\S+", "", text)
    text = re.sub(r"[^a-z\\s]", "", text)
    text = re.sub(r"\\s+", " ", text).strip()
    
    return text

text_files_clean = [clean_text(t) for t in text_files]

df = pd.DataFrame({
    "text": text_files_clean,
    "label": ["Text Files"] * len(text_files_clean)
})

df.to_csv("dataset/cleaned_text_files.csv", index=False, encoding="utf-8")

print("cleaned_text_files.csv is saved to dataset")