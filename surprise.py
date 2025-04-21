#!/usr/bin/env python3


def print_donkey(symbol="#"):
    """
    Prints a stylized donkey ASCII art using the provided symbol.
    You can replace `symbol` with any single ASCII character.
    """
    donkey_template = [
        "    $$    $$",
        "   $  $  $  $",
        "  $    $$    $",
        " $            $",
        "$              $",
        "$              $",
        " $            $",
        "  $          $",
        "   $        $",
        "    $$$$$$$$$$",
    ]
    # Replace placeholder '$' with the chosen symbol and print each line
    for line in donkey_template:
        print(line.replace("$", symbol))


if __name__ == "__main__":
    # Change this symbol to any character you'd like the donkey to be drawn with
    chosen_symbol = "#"
    print_donkey(chosen_symbol)
