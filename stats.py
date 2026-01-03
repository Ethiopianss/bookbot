def get_book_text(path_to_file):
    with open(path_to_file) as f:
        words_number = len(f.read().split())
        return f"Found {words_number} total words"
def character_appearance(path):
    with open(path) as f:
        words = f.read().split()
        characters = {}
        for i in words:
            i = i.lower()
            for j in range(len(i)):
                if i[j] in characters:
                    characters[i[j]] += 1
                else:
                    characters[i[j]] = 1
        return characters
def sort_dict(characters):
    chaar = list(characters.items())
    chaar.sort(key=lambda x: x[1], reverse=True)
    ch = dict(chaar)
    return ch