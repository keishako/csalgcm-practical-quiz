import cleaning_files as cf


folder = "dataset/clean_output"
combined_clean_output = "dataset/WHOLE_calamanCy-result/combined_clean_output.txt"

clean_text_files = cf.load_corpus(folder)

def mergetxt(texts, output_path):
    
    with open(output_path, "w", encoding="utf-8") as combined_file:
        for text in texts:
            cleaned = text.strip()
        if cleaned:
            combined_file.write(cleaned + "\n")

    print("combined_clean_output was created")

if __name__ == "__main__":
    mergetxt(clean_text_files, combined_clean_output)
