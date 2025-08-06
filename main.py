import sys
from stats import get_num_words, get_num_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

word_count =  get_num_words(book_path)
char_count = get_num_chars(book_path)

#print(char_count)

char_list = []
for item in char_count:
    char_list.append({"char":item, "num":char_count[item]})

def sort_key(dict_item):
    return dict_item["num"]

char_list.sort(reverse=True, key=sort_key)

#print(char_list)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for char_dict in char_list:
    if char_dict["char"].isalpha():
        print(f"{char_dict["char"]}: {char_dict["num"]}")
print("============= END ===============")