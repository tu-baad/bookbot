def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_num_characters(text)
    sorted_character_count = character_sort(character_count)
    
    print(f"--- Beginning report of {book_path} ---")
    print()
    print(f"{num_words} words found in the document")
    print()
    print()
    for entry in sorted_character_count:
        print(f"The letter {entry["character"]} was found {entry["count"]} times")
    print()
    print("End of report, have an uwu day ^^")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    character_dict = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1
    
    return character_dict

def character_sort(character_count):

    def sort_on(dict):
        return dict["count"]

    alpha_list = []

    for character in character_count:
        alpha_dict = {}
        if character.isalpha():
           alpha_dict["character"] = str(character)
           alpha_dict["count"] = character_count[character]
           alpha_list.append(alpha_dict)
    
    
    alpha_list.sort(reverse=True, key=sort_on)
    return alpha_list






main()



