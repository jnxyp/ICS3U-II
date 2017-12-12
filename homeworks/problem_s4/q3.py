# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-18
# Problem Set 4 - Question 3


# a)
def parse_rot_13(s: str):
    '''
    (str) -> str
    This function can convert input string with ROT-13 encode method.
    Only the letters in the string will be converted.

    Args:
        s: The string to parse by ROT-13.

    Returns:
        The converted string.
    '''
    s = s.translate(s.maketrans('abcdefghijklmnopqrstuvwxyz', 'nopqrstuvwxyzabcdefghijklm'))
    return s.translate(s.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'NOPQRSTUVWXYZABCDEFGHIJKLM'))


# Test Cases
print('Rot-13: Python ->', parse_rot_13('Python'))
print('Rot-13: Clguba ->', parse_rot_13('Clguba'))


# b)
def encode_caesar(s: str, rot: int):
    '''
    (str, int) -> str
    This function can encode the input string with specific alphabet shift distance.
    Args:
        s: the string to convert.
        rot: the distance to shift on the alphabet.

    Returns:
        The encoded string.
    '''
    out = ''
    for c in s:
        o = ord(c)
        if o >= ord('A') and o <= ord('Z'):
            o = o + rot
            while o > ord('Z'):
                o = o - 26
            while o < ord('A'):
                o = o + 26
        elif o >= ord('a') and o <= ord('z'):
            o = o + rot
            while o > ord('z'):
                o = o - 26
            while o < ord('a'):
                o = o + 26
        out += chr(o)
    return out


# Test Cases
print('Encode: Python + 13 ->', encode_caesar('Python', 13))
print('Encode: Clguba - 13 ->', encode_caesar('Clguba', -13))

print('Encode: Python + 666 ->', encode_caesar('Python', 666))
print('Encode: Fojxed - 666 ->', encode_caesar('Fojxed', -666))


def decode_caesar(s: str, rot: int):
    '''
        (str, int) -> str
        This function can decode the input string with specific alphabet shift distance.
        Args:
            s: the string to convert.
            rot: the distance to shift on the alphabet.

        Returns:
            The decoded string.
    '''
    return encode_caesar(s, -rot)


# Test Cases
print('Decode: Fojxed - 13 ->', decode_caesar('Clguba', -13))
print('Decode: Fojxed + 13 ->', decode_caesar('Python', 13))

