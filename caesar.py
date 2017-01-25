def encrypt(text, rot):
    encrypted = ""
    for x in text:
        rotated = rotate_character(x, rot)
        encrypted += rotated
    return encrypted

def alphabet_position(letter):
    return ord(letter)


def rotate_character(char, rot):
    if char.isalpha():
        if char == char.upper():
            char = alphabet_position(char) + rot
            while char > ord("Z"):
                char -= 26
        else:
            char = alphabet_position(char) + rot
            while char > ord("z"):
                char -= 26
        return chr(char)
    return char
