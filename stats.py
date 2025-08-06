def get_num_words(filepath):
    '''
    takes a filepath to a book in .txt, 
    returns the number fo words in the file
    '''
    with open(filepath) as book_file:
        book_text = book_file.read()
        word_count = len(book_text.split())
    return word_count

def get_num_chars(filepath):
    '''
    takes a filepath to a book in .txt,
    returns a dict counting each character
    '''
    with open(filepath) as book_file:
        book_text = book_file.read().lower()
        char_dict = {}
        for char in book_text:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict
