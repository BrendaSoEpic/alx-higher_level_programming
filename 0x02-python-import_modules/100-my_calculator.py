#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <m> <operator> <n>")
        exit(1)
    m = int(sys.argv[1])
    op = sys.argv[2]
    n = int(sys.argv[3])

    if op is '+':
        print("{} {} {} = {}".format(m, op, n, add(m, n)))
    elif op is '-':
        print("{} {} {} = {}".format(m, op, n, sub(m, n)))
    elif op is '*':
        print("{} {} {} = {}".format(m, op, n, mul(m, n)))
    elif op is '/':
        print("{} {} {} = {}".format(m, op, n, div(m, n)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
