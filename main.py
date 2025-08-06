from stats import get_num_words, get_num_chars

word_count =  get_num_words("books/frankenstein.txt")
print(f"{word_count} words found in the document")

char_count = get_num_chars("books/frankenstein.txt")
print(char_count)