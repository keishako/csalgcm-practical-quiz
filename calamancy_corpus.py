import calamancy
import cleaning_files as cf
import nltk
from nltk.corpus import words

# download if nltk words is not downloaded
nltk.download('words') 

nlp = calamancy.load("tl_calamancy_md", disable=["tagger", "morphologizer", "trainable_lemmatizer","parser"])  # loads the latest version

# used dictionary_set.py
with open("dataset/dictionary/tagalog_word_list.txt", "r", encoding="utf-8") as file:
    tagalog_words = set(line.strip().lower() for line in file if line.strip())

english_words = {w.lower() for w in words.words()}

clean_words_dir = f"dataset/clean_output/"
pnoun_words_dir = f"dataset/proper_noun/"

def normalize_valid_word(token_text):
  normalized = token_text.replace("’", "'").strip("-'") # turn curly apostrophe to standardized one: '
  stripped = normalized.replace("-", "").replace("'", "") # temporarily removes hyphen and apostrophe
  if bool(stripped) and stripped.isalpha():
    return normalized # returns word with apostrophe and hyphen
  return None # skips symbols, punctuation, other unnecessary characters

# START_IDX = 53

for idx, cleaned_text in enumerate(cf.text_files_clean):
    '''
    if idx < START_IDX: # delete when done
        continue
    '''

    clean_words = []        # dataset without proper nouns
    proper_noun_words = []  # proper noun words that are removed (for checking purposes)

    lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()] # split cleaned string into non-empty lines 

    for doc in nlp.pipe(lines, batch_size=512):
        for token in doc:
            text = token.text
            if not text:
                continue

            lower_text = text.lower()
            in_dict = lower_text in tagalog_words
            is_capitalized = token.text[:1].isupper()

            # use calamanCy name detection except when word starts a sentence and normal tagalog word
            is_proper_name = (
                bool(token.ent_type_) 
                and is_capitalized 
                and not (token.is_sent_start and in_dict)
            )

            # start with capital AND NOT the first word of sentence AND NOT normal tagalog words
            is_capital_mid_sentence = (
                is_capitalized 
                and not token.is_sent_start 
                and not in_dict
            )

            if is_proper_name or is_capital_mid_sentence:
                proper_noun_words.append(text)
            else:
                valid_word = normalize_valid_word(lower_text)
                if valid_word and (
                    valid_word in tagalog_words or valid_word not in english_words
                ):
                    clean_words.append(valid_word)       

        # print([(ent.text, ent.label_) for ent in doc.ents])

    clean_words_file = f"clean_output_file_{idx}.txt"
    pnoun_words_file = f"proper_noun_output_file_{idx}.txt"

    with open(clean_words_dir + f"clean_output_file_{idx}.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(clean_words))

    print(f"{clean_words_file} created successfully.")

    with open(pnoun_words_dir + f"proper_noun_output_file_{idx}.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(proper_noun_words))

    print(f"{pnoun_words_file} created successfully.")
