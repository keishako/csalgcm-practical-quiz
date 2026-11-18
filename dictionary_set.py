with open("tagalog_word_list.txt", "r", encoding="utf-8") as file:
  words = {word.lower() for word in file.read().split()}