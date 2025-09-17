from stats import count_words, count_characters, sort_dictionary
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = count_words(text)
        num_characters = count_characters(text)
        ordered_list = sort_dictionary(num_characters)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for dict in ordered_list:
            if dict["char"].isalpha():
                print(f"{dict["char"]}: {dict["num"]}")
        print("============= END ===============")

main()