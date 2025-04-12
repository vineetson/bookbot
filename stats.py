def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def get_num_words(filepath):
    words = get_book_text(filepath).split()
    return len(words)


character_dict = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
    'z': 0, 'æ': 0, 'â': 0, 'ê': 0, 'ë': 0, 'ô': 0
}


def counts(filepath):
    words = get_book_text(filepath).lower()

    for character in words:
        if character in character_dict:
            character_dict[character] += 1

    sorted_by_values_desc = dict(
        sorted(character_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_by_values_desc


''''
✅ 1. Sort by Keys (Alphabetical / Ascending)
python
Copy
Edit
sorted_by_keys = dict(sorted(my_dict.items()))
This gives you a new dictionary sorted by keys.

✅ 2. Sort by Values
python
Copy
Edit
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
You can add reverse=True to sort in descending order:

python
Copy
Edit
sorted_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
🧠 Under the Hood:
dict.items() returns a view of (key, value) tuples.

sorted() is highly optimized in Python (Timsort, O(n log n)).

Example:
python
Copy
Edit
my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sort by keys
print(dict(sorted(my_dict.items())))
# Output: {'a': 1, 'b': 3, 'c': 2}

# Sort by values
print(dict(sorted(my_dict.items(), key=lambda x: x[1])))
# Output: {'a': 1, 'c': 2, 'b': 3}
Let me know what kind of sorting you're aiming for and what data structure you want returned — I can tailor it!
'''
