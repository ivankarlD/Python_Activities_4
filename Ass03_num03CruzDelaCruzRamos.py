
input_str = input("Insert text: ")


def flipEndCharacter(input_str):
    # Check if string has only one character
    if len(input_str) == 1:
       print("Incompatible.")

    elif input_str[0] == input_str[-1]:
        print("Two's a pair.")

    else:
        # Swap the first and last character
        first_char = input_str[0]
        last_char = input_str[-1]
        middle_chars = input_str[1:-1]
        new_str = last_char + middle_chars + first_char

        # Print the new string
        print(new_str)


flipEndCharacter(input_str)
