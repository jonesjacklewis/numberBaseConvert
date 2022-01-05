"""This program converts from any number base (<60) to base 10"""


def get_int_input(prompt: str = "Enter an integer: ") -> int:
    """Method to get an integer input from the user.
    
    Keyword arguments:
        prompt: str -- The message to be outputted to the user.
    Return:
        to_return: int -- The integer the user inputs.
    """

    to_return = "invalid_input"

    while not to_return.isnumeric():
        to_return = input(prompt)


    return int(to_return)

def load_table(base: int = None) -> dict:
    """Method to get the convertion table for number bases.
    
    Keyword arguments:
        base: int = None -- The number base to convert from.
    Return:
        table: dict -- A dictionary to convert to base 10.
    """
    with open("translation-table.csv", "r") as f:
        table = [line.strip().split(",") for line in f.readlines()]

        table = {row[0]: int(row[1]) for row in table}

    if base:
        return dict(list(table.items())[:base])
    else:
        return table
    
def convert(table: dict, base: int, original: str) -> int:
    """Method to convert from the supplied base to base 10.
    
    Keyword arguments:
        table: dict -- The conversion table for the number base.
        base: int -- The number base to convert from.
        original: str -- The number to convert to base 10.
    Return:
        converted: int -- The base 10 value.
    """
    return sum(
        table[character[1]] * (base ** character[0])
        for character in enumerate(original[::-1])
    )


def main():
    base = get_int_input("Enter the base to convert from: ") # e.g. 16 for hexadecimal
    table = load_table(base) # e.g. would load the table containing conversions such as 0=1,1=1...15=F
    number_to_convert = input("Enter the number to convert: ") # e.g. ABC
    base10 = convert(table, base, number_to_convert) # e.g. 2748

    print(f"The base {base} number {number_to_convert} is equal to {base10} in base 10.")

if __name__ == '__main__':
    main()
