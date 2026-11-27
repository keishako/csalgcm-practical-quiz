import cleaning_files as cf

folder = "dataset/clean_output"
combined_clean_output = "dataset/WHOLE_calamanCy-result/combined_clean_output.txt"

clean_text_files = cf.load_corpus(folder)

def mergetxt(texts, output_path):
    
    with open(output_path, "w", encoding="utf-8") as combined_file:
        combined_file.write("\n".join(texts))

    print("combined_clean_output.txt was created")


mergetxt(clean_text_files, combined_clean_output)

