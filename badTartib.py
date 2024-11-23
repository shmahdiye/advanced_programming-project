import string


def main():
    input_str = "Salam salam chetori? Che khabara? :D"
    input_str = remove_spaces(input_str)
    sort(input_str)


def sort(input_str):
    letters, numbers, special_chars = [], [], []
    for char in input_str:
        if char in string.ascii_letters:
            letters.append(char)
        elif char in string.digits:
            numbers.append(char)
        else:
            special_chars.append(char)

    sorted_output = ''.join(special_chars) + \
                    ''.join(sorted(numbers)) + \
                    ''.join(sorted(letters, key=lambda char: char.lower()))
    print(sorted_output)


def remove_spaces(input_str):
    input_str = ''.join(input_str.split())
    return input_str


if __name__ == '__main__':
    main()
