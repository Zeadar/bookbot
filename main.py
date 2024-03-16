def main():
    words = get_book("./books/frankenstein.txt").lower().split()
    #characters = [w.lower() for w in words]
    #print("letters", characters)
    print("amount of words", len(words))
    
    char_count = {}

    for w in words:
        for c in w:
            if not c.isalpha():
                continue
            if (c in char_count):
                char_count[c] += 1
            else:
                char_count[c] = 1

    char_count = [{"letter": key, "num": char_count[key]} for key in char_count]
    char_count.sort(key=get_num, reverse=True)
    #print("character count", word_count)

    for d in char_count:
        print(d["letter"], d["num"])


def get_num(d):
    return d["num"]

def get_book(path):
    with open(path) as file:
        return file.read()
    
main()
