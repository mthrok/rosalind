from __future__ import division
from __future__ import print_function

import time
from math import log


def preprocess(string):
    return int(string.strip())


def comb(n, k):
    k = min(k, n-k)
    ret = 1
    for i in range(k):
        ret *= n-i
    for i in range(k):
        ret //= i+1
    return ret


def binom(n, k, p=0.5):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))


def solve(n):
    cum = 1
    A = [0] * (2 * n)
    for i in range(2 * n):
        cum -= binom(2 * n, i)
        A[i] = log(cum, 10)
    return ' '.join(map(lambda val: '{:05.3f}'.format(val), A))


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
    t0 = time.time()
    ret = solve(data)
    t1 = time.time()
    print('*OUTPUT ({} [sec])*\n{}'.format(t1-t0, ret))


if __name__ == '__main__':
    main()
