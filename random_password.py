"""
Create a 8 character long password that also has
the following characteristics:
        1-2 special characters
        1-2 digits
        1/3 Upper digits
        Remaining upper digits """
import random
from itertools import permutations
from numpy import array


def selector(num, arr, chosen_ones):
    for _ in range(num):
        chosen_ones.append(random.choice(arr))


spec_char = ['!', '@', '#', '$', '&']

digits = [str(i) for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = [i.upper() for i in lower_letters]


def password_maker(t=True):
    no_spec = random.choice(range(1, 3))
    no_digits = random.choice(range(1, 3))
    no_letters = 8 - no_spec - no_digits
    no_upper = no_letters // 3
    no_lower = no_letters - no_upper

    chosen_ones = []

    selector(no_spec, spec_char, chosen_ones)
    selector(no_digits, digits, chosen_ones)
    selector(no_upper, upper_letters, chosen_ones)
    selector(no_lower, lower_letters, chosen_ones)

    random.shuffle(chosen_ones)
    chosen_ones = ''.join(chosen_ones)
    if t:
        print('Your newly generated password is: ', chosen_ones)
    else:
        return chosen_ones


password_maker()
