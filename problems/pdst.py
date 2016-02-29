from __future__ import division
from __future__ import print_function

import numpy as np


def preprocess(string):
    data = string.strip().split('>')[1:]
    return [''.join(datum.split('\n')[1:]) for datum in data]


def pdist(string1, string2):
    l_str = len(string1)
    if l_str != len(string2):
        raise RuntimeError('String lengths are not equal.')
    count = 0
    for c1, c2 in zip(string1, string2):
        if c1 != c2:
            count += 1
    return count / l_str


def solve(strings):
    n_strs = len(strings)
    mat = np.zeros((n_strs, n_strs))
    for r in range(n_strs):
        for c in range(r+1, n_strs):
            d = pdist(strings[r], strings[c])
            mat[r][c] = d
            mat[c][r] = d
    ret = ''
    for row in mat:
        ret += '{}\n'.format(
            ' '.join(map(lambda val: '{:7.5f}'.format(val), row)))
    return ret


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
