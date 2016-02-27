from __future__ import division
from __future__ import print_function

from math import log


def preprocess(string):
    data = string.strip().split('\n')
    string = data[0]
    A = map(float, data[1].split(' '))
    return string, A


def compute_prob(string, gc_ratio):
    prob = {
        'A': (1 - gc_ratio) / 2,
        'T': (1 - gc_ratio) / 2,
        'C': gc_ratio / 2,
        'G': gc_ratio / 2,
    }
    ret = 1.0
    for char in string:
        ret *= prob[char]
    return ret


def solve((string, A)):
    ret = []
    for gc_ratio in A:
        prob = compute_prob(string, gc_ratio)
        ret.append(log(prob, 10))
    return ' '.join(map(str, ret))


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
