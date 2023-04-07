
import re

TOKENS = [
    (re.compile(r'\bif\b'), 'KEYWORD'),
    (re.compile(r'\belse\b'), 'KEYWORD'),
    (re.compile(r'\bwhile\b'), 'KEYWORD'),
    (re.compile(r'\bfor\b'), 'KEYWORD'),
    (re.compile(r'\bint\b'), 'KEYWORD'),
    (re.compile(r'\bfloat\b'), 'KEYWORD'),
    (re.compile(r'\bdouble\b'), 'KEYWORD'),
    (re.compile(r'[0-9]+\.[0-9]+'), 'REAL'),
    (re.compile(r'[0-9]+'), 'INTEGER'),
    (re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*'), 'IDENTIFIER'),
    (re.compile(r'[=+\-*/<>=]'), 'OPERATOR'),
    (re.compile(r'[;{},()]'), 'SEPERATOR'),
    (re.compile(r'//.*?$'), 'COMMENT'),
    (re.compile(r'/\*.*?\*/', re.DOTALL), 'COMMENT'),
    (re.compile(r'\s+'), 'WHITESPACE')
]


def lexer(filename):
    with open(filename, 'r') as f:
        source_code = f.read()

    tokens = []
    i = 0

    while i < len(source_code):
        match = None
        for regex, token in TOKENS:
            match = regex.match(source_code[i:])
            if match:
                value = match.group()
                if token == 'WHITESPACE':
                    i += len(value)
                    break
                tokens.append((token, value))
                i += len(value)
                break
        else:
            print('Invalid token at %d' %i)
            print(source_code[i:])
            i += 1

    return tokens


tokens = lexer('input_scode.txt')

with open('output.txt', 'w') as f:
    f.write("Token\t\t|\tLexeme\n")
    for token, lexeme in tokens:
        f.write(f'{token}\t\t|\t{lexeme}\n')
