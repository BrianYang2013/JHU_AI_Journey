def backwards_alphabet(curr_letter):
    if curr_letter == 'a':
        print(curr_letter)
    else:
        print(curr_letter)
        prev_letter = chr(ord(curr_letter) - 1)
        backwards_alphabet(prev_letter)

starting_letter = input("Pick a start letter: ")
backwards_alphabet(starting_letter)
