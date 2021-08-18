# Program name: stegsnow.py

import sys

CHARACTER_LENGTH = 7    # Length of a binary character
ZERO = '\t'              # Character representing zero         ``
ONE = ' '              # Character representing one

CHAR_TO_BINARY = { # binary representation of ASCII characters
    'a': '1100001', 
    'b': '1100010',
    'c': '1100011',
    'd': '1100100', 
    'e': '1100101',
    'f': '1100110',
    'g': '1100111',
    'h': '1101000',
    'i': '1101001',
    'j': '1101010',
    'k': '1101011',
    'l': '1101100',
    'm': '1101101',
    'n': '1101110',
    'o': '1101111',
    'p': '1110000',
    'q': '1110001',
    'r': '1110010',
    's': '1110011',
    't': '1110100',
    'u': '1110101',
    'v': '1110110',
    'w': '1110111',
    'x': '1111000',
    'y': '1111001',
    'z': '1111010',
    ' ': '1111011'
}

BINARY_TO_CHAR = { # binary string to ascii characters
    '1100001': 'a', 
    '1100010': 'b',
    '1100011': 'c',
    '1100100': 'd', 
    '1100101': 'e',
    '1100110': 'f',
    '1100111': 'g',
    '1101000': 'h',
    '1101001': 'i',
    '1101010': 'j',
    '1101011': 'k',
    '1101100': 'l',
    '1101101': 'm',
    '1101110': 'n',
    '1101111': 'o',
    '1110000': 'p',
    '1110001': 'q',
    '1110010': 'r',
    '1110011': 's',
    '1110100': 't',
    '1110101': 'u',
    '1110110': 'v',
    '1110111': 'w',
    '1111000': 'x',
    '1111001': 'y',
    '1111010': 'z',
    '1111011': ' '
}

def small_message_encoder(message, infile, outfile, zero, one):
    """Encode the secret message at the end of each line in input file and write 
    the file containing the secret message to the outfile. This function will
    only encode the secret message up until the number of characters is equal to
    the number of lines in input file.  

    Args:
        message (str): Message to be embedded in infile.
        infile (str): Input file name.
        outfile (str): Output file name.
        zero (str): Character representing a zero.
        one (str): Character representing a one.

    Returns:
        int: Represents all the characters from message[0] to message[index-1] 
        that have been encoded.
    """

    index = 0 # used to traverse the message string
    with open(infile, "r") as i_file, open(outfile, "w") as o_file: # open files
        for line in i_file: # go through the input file line by line
            # when number of lines > than length of message, only line is added
            if index >= len(message): 
                o_file.write(line)
            else: # modify to encode the message at the end of each input line
                o_file.write(line[:-1] + encode(CHAR_TO_BINARY[message[index]],\
                                                             zero, one) + "\n")
                index += 1 # increment index by 1
    return index
    

def long_message_encoder(message, outfile, zero, one, index):
    """Encode remaining secret message when message is longer than number of 
    lines in infile and write the encoded message to the outfile. 

    Args:
        message (str): Message to be embedded in infile.
        outfile (str): Output file name.
        zero (str): Character representing a zero.
        one (str): Character representing a one.
        index (int): Initial index from which encoding needs to take place from. 
    """

    with open(outfile, "a") as o_file: # open file in append mode 
        # go through the remaining characters in the string and encode and write
        # each character's binary string on a new line
        for i in range(index, len(message), 1): 
            o_file.write(encode(CHAR_TO_BINARY[message[i]], zero, one) + "\n")


def encode_secret_message(message, infile, outfile, zero, one):
    """Encode the secret message in input file file, write the file containing
    the secret message to the outfile.           
 
    Args:
        zero (str): Character representing a zero.
        one (str): Character representing a one.
        message (str): Message to be embedded in infile.
        infile (str): Input file name.
        outfile (str): Output file name.
    """

    # call small_message_encoder() when number of lines in file is more than or 
    # equal to length of message
    # setting index to 0 because starting from the beginning of the string
    index = small_message_encoder(message, infile, outfile, zero, one)

    # value of index-1 indicates the characters which have been encoded in the 
    # output file 
    # if index < length of message, it means full message is not encoded yet
    if index < len(message):
        long_message_encoder(message, outfile, zero, one, index)


def encode(binary_letter, zero_char, one_char):
    """Make the message invisible. Substitute the zeroes and ones in binary 
        letter for your chosen characters, typically tab and space.

    Args:
        binary_letter (str): a sequence of zeroes and ones representing an ascii character.
        zero_char (str): The character with which the zeroes should be replaced.
        one_char (str): The character with which the ones should be replaced.

    Returns:
        str: Represents the letter.
    """

    return binary_letter.replace('0', zero_char).replace('1', one_char)


def decode(binary_letter, zero_char, one_char):
    """Make the message visible. Substitute the characters representing zeroes and ones in the binary 
        letter for the characters '0' and '1'.

    Args:
        encoded_char (str): a sequence of zeroes and ones.
        zero_char (str): The character to be replaced with zeroes.
        one_char (str): The character to be replaced with ones.

    Returns:
        str: Represents the letter.
    """

    return binary_letter.replace(zero_char, '0').replace(one_char, '1')


def decode_secret_message(infile, zero, one):
    """Print the decoded message in the file infile

    Args:
        infile (str): file name
        zero_char (str): The character with which the zeroes should be replaced.
        one_char (str): The character with which the ones should be replaced.
    """
    
    message = '' # message holds the secret message 
    with open(infile, "r") as i_file: # open file
        for line in i_file: # go through the input file line by line
            # decode last 7 characters of line before \n
            binary_string = decode(line[-8:-1], zero, one) 
            if set(binary_string) == {'0', '1'}: 
                message += BINARY_TO_CHAR[binary_string] 
    print(message) # print final message as a string


def main():

    zero = ZERO 
    one = ONE

    args = sys.argv[1:]                      
    if len(args) != 1 and len(args) != 4:
        print(f'usage: \n\tto encode a message: python stegsnow.py -m "message" infile outfile\
            \n\t\t*infile is okonomiyaki.txt\
            \n\t\t*outfile is .txt file containing the encoded secret message\
            \n\n\tto decode a message: python stegsnow.py infile\
            \n\t\t*infile is .txt file containing the encoded secret message (outfile)\
            \n\n*a secret message must be encoded first to see the decoded the message')
        return
 
    # Parse message, infile, outfile from command line, giving a helpful
    # error message if this fails.

    try:
        if len(args) == 1:
            encoded_file = args[0]
        elif len(args) == 4:
            message = args[1]
            plaintext_file = args[2]
            output_file = args[3]
        else:
            raise ValueError
    except Exception:
        print("Error parsing options from command line: " + ' '.join(args))
        return

    if args[0] == '-m':
        encode_secret_message(message, plaintext_file, output_file, zero, one)
    else:
        decode_secret_message(encoded_file, zero, one)
    

if __name__ == "__main__":
    main()