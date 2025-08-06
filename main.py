with open("books/frankenstein.txt") as book_file:
    book_text = book_file.read()
    #print(book_text)
    word_count = len(book_text.split())
    print(f"{word_count} words found in the document")