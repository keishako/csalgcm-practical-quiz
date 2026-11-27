import os
import re
# import pandas as pd

dataset_path = r"dataset/text_files"

other_language = re.compile('[^\u0020-\u024F\n]')

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
    # text = text.lower()
    text = re.sub(r"https?://\S+", "", text)
    text = other_language.sub("", text)
    text = re.sub(r'[^\w\d\s\'\-]+', "", text) #includes words with hyphen and apostrophe
    text = re.sub(r"[ \t]+", " ", text).strip()
    
    return text

text_files_clean = [clean_text(t) for t in text_files]
print("text_files_clean is initialized")



'''
df = pd.DataFrame({
    "text": text_files_clean,
    "label": ["Text Files"] * len(text_files_clean)
})

# df.to_csv("dataset/cleaned_text_files.csv", index=False, encoding="utf-8")
with open("dataset/cleaned_text_files.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(text_files_clean))

print("cleaned_text_files.txt is saved to dataset")
'''