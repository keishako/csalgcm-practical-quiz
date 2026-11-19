# Importing the required libraries
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize

# Function to extract the proper nouns 

def ProperNounExtractor(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.read()
    
    print('PROPER NOUNS EXTRACTED :')
    
    sentences = nltk.sent_tokenize(lines)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if tag == 'NNP': # If the word is a proper noun
                print(word)

# Calling the ProperNounExtractor function to extract all the proper nouns from the given text. 
if __name__ == "__main__":
    ProperNounExtractor('output_file_50.txt')