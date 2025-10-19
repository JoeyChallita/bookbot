def count_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(char_count):
    list_d = []
    for key, value in char_count.items():
        list_d.append({"char": key, "num": value})
    list_d.sort(reverse=True, key=sort_on)
    return list_d


def sort_on(item):
    return item["num"]
