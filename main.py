from art import logo

# entry list of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# a function for encode/decode
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # allow special characters and numbers
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            if new_position > len(alphabet):
                new_position = new_position % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


# print the logo from art.py when the program starts.
print(logo)


# make program repeat unless decided by user
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # check if the entered shift number is higher than length of list of letters so the remaining restarts from 0
    # if shift > (len(alphabet)):
    #    shift = shift % len(alphabet)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # condition for repeat/no repeat
    resume = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if resume == 'no':
        should_continue = False
        print("GoodBye !")
