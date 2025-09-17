def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    d = {}
    all_lowercase = book_text.lower()
    for character in all_lowercase:
        if character not in d.keys():
            d[character] = 1
        else:
            d[character] += 1
    return d

def sort_on(d_list):
    return d_list["num"]

def sort_dictionary(dictionary):
    print("============ BOOKBOT ============")
    print("Analyzing book found at GET VIA VARIABLE...")
    print("----------- Word Count ----------")
    print("Found GET VIA VARIABLE total words")
    print("--------- Character Count -------")
    l = []
    for key in dictionary:
        new_d = {"char": key, "num": dictionary[key]}
        l.append(new_d)
    l.sort(reverse=True, key=sort_on)
    return l

