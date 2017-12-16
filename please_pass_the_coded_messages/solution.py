"""Solution to Google challenge Please Pass the Coded Messages"""
import itertools


def get_combinations(l, length):
    """Returns all combinations of a list for a given length."""
    combinations = list(itertools.combinations(l, length))
    return combinations


def get_permutations(l):
    """Returns all permutations of a list."""
    permutations = list(itertools.permutations(l))
    return permutations


def join_integers(t):
    """Joins integers in list. Accepts tuple of integers. Returns joined integer."""
    joined_integer = int("%i" * len(t) % (t))
    return joined_integer


def find_largest_integer(l, divisor=3):
    """Finds largest int divisible by certain number. Accepts list of integers.
    Returns largest or 0 if not found in list."""
    l.sort(reverse=True)

    for i in l:
        if i != 0 and i % divisor == 0:
            return i

    return 0


def answer(l):
    """Main function. Accepts list of integers.
    Returns the largest number that these digits can form that is divisible by 3."""
    current_largest = 0

    for length in range(len(l), 0, -1):
        combinations = get_combinations(l, length)
        combinations.sort(reverse=True)

        for combination in combinations:
            permutations = get_permutations(list(combination))
            integer_list = [join_integers(p) for p in permutations]
            largest_integer = find_largest_integer(integer_list, 3)

            if largest_integer > current_largest:
                current_largest = largest_integer

    return current_largest
