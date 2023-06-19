def generate_char_array(char_type):
    if char_type == 'lowercase':
        char = [chr(code) for code in range(ord('a'), ord('z') + 1)]
    elif char_type == 'uppercase':
        char = [chr(code) for code in range(ord('A'), ord('Z') + 1)]
    elif char_type == 'digits':
        char = [chr(code) for code in range(ord('0'), ord('9') + 1)]
    else:
        char = [chr(code) for code in range(ord('!'), ord('/') + 1)] + \
               [chr(code) for code in range(ord(':'), ord('@') + 1)] + \
               [chr(code) for code in range(ord('['), ord('`') + 1)] + \
               [chr(code) for code in range(ord('{'), ord('~') + 1)]
    return char