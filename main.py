from env import global_env,eval
from lisp_parser import parse
def repl(prompt='lisp.py>'):
    """ a prompt-read-eval-print loop"""
    while True:
        val = eval(parse(input(prompt)), global_env)
        # parse()
        if val is not None:
            print(liststr(val))

def liststr(exp):
    """convert a python object back into a Lisp-readable string."""
    if isinstance(exp, list):
        return '(' + ' '.join(map(liststr,exp)) + ')'
    else:
        return str(exp)
if __name__ == '__main__':
    # print(parse(input("lisp.py")))
    # list_test = ['*', ['+', [2, 3]], ['+', [3, ['define', 'pi', 3.14]]]]
    # string_test = "(*(+(2 3)) (+ (3 (define pi 3.14)) ))"
    # test = liststr(list_test)
    # print(test)
    repl()