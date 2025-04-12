import sys
import stats
from stats import get_num_words, counts


def main():
    print('============ BOOKBOT ============')
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    print(f"Analyzing book found at {filepath}...")
    count = get_num_words(filepath)

    print('----------- Word Count ----------')
    print(f"Found {count} total words")

    print("--------- Character Count -------")
    count_dict = counts(filepath)

    for i in count_dict:
        print(f'{i}: {count_dict[i]}')

    print("============= END ===============")


main()
'''
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
'''
