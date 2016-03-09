from __future__ import division
from __future__ import print_function


def preprocess(string):
    return list(map(int, string.strip().split(' ')))


def factorial(n):
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret


def comb(n, k):
    if n-k < k:
        k = n-k
    ret = 1
    for i in range(k):
        ret *= n - i
    ret //= factorial(k)
    return ret


def solve((n, m)):
    mod = 1000000
    ret = 0
    for k in range(m, n+1):
        ret += comb(n, k) % mod
    return ret % mod


def parse_command_line_arguments():
    import os
    default_input = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'dataset',
        'rosalind_{}.txt'.format(__file__.split('/')[-1].split('.')[0]))
    from argparse import ArgumentParser as AP
    ap = AP()
    ap.add_argument('--input', default=default_input)
    return ap.parse_args()


def main():
    args = parse_command_line_arguments()
    data = preprocess(open(args.input, 'r').read())
    print('*INPUT*\n{}\n'.format(data))
    ret = solve(data)
    print('*OUTPUT*\n{}'.format(ret))


if __name__ == '__main__':
    main()
