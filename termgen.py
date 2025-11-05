import random
import argparse

def generate(n_nodes: int, n_inputs: int, operators: list[tuple[str, int]]):
    consts = [op for op, arity in operators if arity == 0]
    operators = [(op, arity) for op, arity in operators if arity != 0]

    def recurse(n: int):
        if n == 0:
            if consts and random.choice([True, False]):
                return '(' + random.choice(consts) + ')'
            else:
                input = random.choice(range(n_inputs))
                return f'v{input}'

        else:
            op, arity = random.choice(operators)
            sub = ()
            n = n - 1
            for i in range(arity - 1):
                size = random.choice(range(n + 1))
                sub += (recurse(size), )
                n = n - size
            return (op,) + sub + (recurse(n), )
    return recurse(n_nodes)


parser = argparse.ArgumentParser(description='Generate random terms')
parser.add_argument('-n', '--nodes', type=int, required=True, help='number of interior nodes')
parser.add_argument('-i', '--inputs', type=int, required=True, help='number of inputs')
parser.add_argument('-o', '--operators', type=str, required=True, help='operators with their arities (e.g. add:2,sub:2,neg:1)')
args = parser.parse_args()

ops = [ a.split(':') for a in args.operators.split(',') ]
ops = [ (f.strip(), int(a.strip())) for f, a in ops ]

res = generate(args.nodes, args.inputs, ops)
res = str(res).replace(',', '').replace(r"'", '')
print(res)

