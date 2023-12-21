def get_symbol_frequency(s: str) -> dict[str, float]:

    """
    calculates frequency of a symbol in a string

    :param s: input string
    :return: dictionary of char and frequency
    """

    length = len(s)
    res = {}
    for char in set(s):
        res[char] = round(s.count(char) * 100 / length, 2)

    return res


def get_ternary(x: int, y: int) -> str | int:

    """
    runs logic using ternary operator
    """

    return x + y if x < y else x - y if x > y else 'game over' if x == 0 and y == 0 else 0


if __name__ == '__main__':

    print(get_symbol_frequency('qwerty 111111111 aaaaaaa'))

    for operand_1, operand_2 in (0, 0), (10, 20), (20, 10), (10, 10):
        print(get_ternary(operand_1, operand_2))
