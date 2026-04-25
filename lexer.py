import ply.lex as lex

tokens = (
    'COMMENT',
    'OPEN_TAG',
    'CLOSE_TAG',
    'SELF_CLOSE',
    'TEXT'
)

# Token rules
t_COMMENT    = r'<!--.*?-->'
t_SELF_CLOSE = r'<[a-zA-Z]+(?:\s+[a-zA-Z]+="[^"]*")?\s*/>'
t_OPEN_TAG   = r'<[a-zA-Z]+>'
t_CLOSE_TAG  = r'</[a-zA-Z]+>'
t_ignore     = ' \t\n'

def t_TEXT(t):
    r'[^<]+'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
