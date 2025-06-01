def encrypted_message(): # A function which perform an encryption

    key = input("Enter a 6-character encryption key: ") # TheKey

    if key >= str(6) or key == str(6):
        message = input("Enter a message to encrypt: ") # abcdefghijklmnopqrstuv

    def pad_message(message): # The helper function to pad the message
        while len(message) % 8 != 0:
            message += "a"
        return message
    print(pad_message(message))

    def split_message(message): # Split the message
        return [message[i:i+8] for i in range(0, len(message), 8)]
    print(split_message(pad_message(message)))

    def calculate_shift1(key): # Calculate first shift
        shift1 = (ord(key[0])+ ord(key[1])) % 8
        return shift1
    print(calculate_shift1(key))

    def right_cyclic_shift(sequence, shift): # Shift
        return sequence[-shift:] + sequence[:-shift]

    def apply_shift1(subsequences, shift1): # Applying the shift
        return [right_cyclic_shift(seq, shift1) for seq in subsequences]
    print(apply_shift1(split_message(pad_message(message)), calculate_shift1(key)))

    def calculate_shift2(key): # Calculate second shift
        shift2 = (ord(key[3]) + ord(key[4])) % 3
        return shift2
    print(calculate_shift2(key))

    def apply_shift2(subsequences, shift2): # Applying second shift
        return subsequences[-shift2:] + subsequences[:-shift2]
    print(apply_shift2(apply_shift1(split_message(pad_message(message)), calculate_shift1(key)), calculate_shift2(key)))

    def concatenate_subsequences(subsequences): # Final encrypted message
        return "".join(subsequences)
    print(concatenate_subsequences(apply_shift2(apply_shift1(split_message(pad_message(message)), calculate_shift1(key)), calculate_shift2(key))))


encrypted_message() # Calling the function to encrypt the message










