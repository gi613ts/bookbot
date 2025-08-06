def get_num_words(filepath):
    '''
    takes a filepath to a book in .txt, 
    returns the number fo words in the file
    '''
    with open(filepath) as book_file:
        book_text = book_file.read()
        word_count = len(book_text.split())
    return word_count