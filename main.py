def main():
    book = get_book("./books/frankenstein.txt")
    words = book.lower().split()
    #characters = [w.lower() for w in words]
    #print("letters", characters)
    print("amount of words", len(words))
    
    word_count = {}

    for w in words:
        for c in w:
            if (c in word_count):
                word_count[c] += 1
            else:
                word_count[c] = 1

    print("character count", word_count)

def get_book(path):
    with open(path) as file:
        return file.read()
    


main()
