def tokenize(chars):
    """convert a string of characters into a list of tokens."""
    return chars.replace('(',' ( ').replace(')',' ) ').split()


def parse(program):
    """read a scheme expression from a string"""
    return  read_form_tokens(tokenize(program))

def atom(token):
    """ numbers become numbers; every other tokens is a symbol"""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)


def read_form_tokens(tokens):
    """read an expression from a sequence of tokens. """
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_form_tokens(tokens))
        tokens.pop(0)
        return L 
    elif token == ')':
        raise SyntaxError('unexpected )')
    else:
        return atom(token)



