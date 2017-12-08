import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()
registers = defaultdict(int)


def eval_cond(lhs, sym, rhs):
    import operator
    table = {
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '==': operator.eq,
            '!=': operator.ne
            }
    if sym not in table:
        raise Exception("unknown operator {}".format(sym))

    return table[sym](registers[lhs], int(rhs))


def do_line(line):
    reg, sgn, inc_qty, _, cond_lhs, cond_symb, cond_rhs = line.split()

    if eval_cond(cond_lhs, cond_symb, cond_rhs):
        inc_qty = int(inc_qty)
        if sgn == "dec":
            inc_qty = -inc_qty
        registers[reg] += inc_qty

    return max(registers.values())


print([do_line(line) for line in lines][-1])
