import sys 
def main():
    from stats import get_book_text,count_the_characters,count_the_words,creating_a_list
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_book = sys.argv[1]
    pathing = get_book_text(path_to_book)
    num_words = count_the_words(pathing)
    num_char = count_the_characters(pathing)
    sorted_list = creating_a_list(num_char)
    print(f"Found {num_words} total words")
    for listings in sorted_list:
        print(f"{listings["char"]}: {listings["num"]}")

main()
