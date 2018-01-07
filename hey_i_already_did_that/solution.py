"""Solution to Google challenge Hey, I Already Did That!"""

def decimal_to_base(i, b):
    """Converts decimal integer to base b.
    Returns result as string."""
    result = []

    while i > 0:
        result.insert(0, i % b)  # insert modulo into result list at index 0
        i = i / b

    result = ''.join([str(i) for i in result])  # squash list together as string
    return result


def answer(n, b):
    """Main answer function. Arguments:

    n = minion ID, a nonnegative integer of length k as string.
    b = base of minion ID.

    Returns the length of the ending cycle of the described algorithm
    starting with n. Returns 1 when a constant is reached."""

    results = []
    k = len(n)  # length of n

    while n not in results:
        results.append(n)  # append n to results
        x = int(''.join(sorted(list(n), reverse=True)), b)  # n in descending order as base b int
        y = int(''.join(sorted(list(n))), b)  # n in ascending order as base b int
        z = decimal_to_base(x - y, b)  # result of x - y converted to base b
        z = z.zfill(k)  # leftpad with zeroes if necessary
        n = z  # assign z to n and repeat

    # Return 1 if a constant is reached:
    if n == results[-1]:
        return 1

    # Otherwise, return length of of ending cycle:
    index = results.index(n)
    return len(results[index:])
