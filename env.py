import math
import operator as op

def standard_env():
    """ An environment with some Scheme standard procedures. """
    env = Env()
    env.update(vars(math))
    env.update({
        '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv,
        '>': op.gt, '<': op.lt ,'>=': op.ge, '<=': op.le, '=': op.eq,
        'abs': abs,
        'append': lambda x, y: x + y,
        'apply': lambda proc, args: proc(*args),
        'begin': lambda *x: x[-1],
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x] + y,
        'eq?': op.is_,
        'expt': pow,
        'equal?': op.eq,
        'length': len,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'map': lambda proc, lst: list(map(proc, lst)),
        'max': max,
        'min': min,
        'not': op.not_,
        'null?': lambda x: x == [],
        'number?': lambda x: isinstance(x, (int, float)),
        'procedure?': callable,
        'round': round,
        'symbol?': lambda x: isinstance(x, str),
    })
    return env

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var):
        "Find the innermost Env where var appears."
        # print(self)
        return self if (var in self) else self.outer.find(var)

def eval(x, env):
    """evaluate an expression in an environment"""
    if isinstance(x,str):
        return env.find(x)[x]
    elif not isinstance(x,list):
        return x
    elif x[0] == 'quote':
        (_,exp) = x
        return exp
    elif x[0] == 'if':
        (_,test,conseq,alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':
        (_, var, exp) = x
        env[var] = eval(exp, env)
    elif x[0] == 'set!':
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif x[0] == 'lambda':
        (_, parms, exp) = x
        return lambda *args: eval(exp, Env(parms, args, env))
    else:
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)
global_env = standard_env()
# e_find = Env(parms=('pi', 'e'),args=(3.14, 2.71),outer= global_env)

# print(e_find)
# print(e_find.find('+'))

