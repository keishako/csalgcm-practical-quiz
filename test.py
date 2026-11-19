def split_file(file_path, lines_per_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for file_count, i in enumerate(range(0, len(lines), lines_per_file), start=1):
        output_filename = f'output_file_{file_count}.txt'
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines[i:i+lines_per_file])
        print(f"{output_filename} created successfully.")

if __name__ == "__main__":
    split_file('Raw.txt', 6513)