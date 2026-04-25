import ply.yacc as yacc
from lexer import tokens

# ---------- 1. VALID COMMENT ----------
def p_comment(p):
    'comment : COMMENT'
    print("✅ Valid Comment")

# ---------- 2. MATCHING TAG PAIRS ----------
def p_matching(p):
    'matching : OPEN_TAG TEXT CLOSE_TAG'
    open_tag = p[1][1:-1]
    close_tag = p[3][2:-1]
    if open_tag == close_tag:
        print("✅ Accepted: Matching Tags")
    else:
        print("❌ Rejected: Tags do not match")

# ---------- 3. TABLE STRUCTURE ----------
def p_table(p):
    '''table : OPEN_TAG OPEN_TAG OPEN_TAG TEXT CLOSE_TAG CLOSE_TAG CLOSE_TAG'''
    open_tags = [p[1][1:-1], p[2][1:-1], p[3][1:-1]]
    close_tags = [p[7][2:-1], p[6][2:-1], p[5][2:-1]]
    if open_tags == close_tags == ['table','tr','td']:
        print("✅ Accepted: Valid Table Structure")
    else:
        print("❌ Rejected: Invalid Table Structure")

# ---------- 4. SELF-CLOSING TAG ----------
def p_selfclose(p):
    'selfclose : SELF_CLOSE'
    print("✅ Valid Self-Closing Tag")

# ---------- 5. HEAD & BODY ----------
def p_headbody(p):
    'headbody : OPEN_TAG TEXT CLOSE_TAG OPEN_TAG TEXT CLOSE_TAG'
    tags = [p[1][1:-1], p[3][2:-1], p[4][1:-1], p[6][2:-1]]
    if tags == ['head', 'head', 'body', 'body']:
        print("✅ Accepted: Valid Head & Body Structure")
    else:
        print("❌ Rejected: Invalid Head & Body Structure")

def p_error(p):
    print("❌ Rejected: Invalid syntax or structure")

# Build all parsers
def build_parser(start_rule):
    return yacc.yacc(start=start_rule, debug=False, write_tables=False, errorlog=yacc.NullLogger())

parsers = {
    'comment': build_parser('comment'),
    'matching': build_parser('matching'),
    'table': build_parser('table'),
    'selfclose': build_parser('selfclose'),
    'headbody': build_parser('headbody')
}
