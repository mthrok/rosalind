from __future__ import division
from __future__ import print_function

from collections import Counter


def preprocess(string):
    return ''.join(string.strip().split('>')[1].split('\n')[1:])


def k_mer(k):
    ret = []
    alphabet = 'ACGT'
    for i in range(4 ** k):
        mer = ''
        for _ in range(k):
            mer += alphabet[i % 4]
            i //= 4
        ret.append(mer)
    return ret


def solve(string):
    c = Counter()
    for i in range(0, len(string)-3):
        substring = string[i:i+4]
        c[substring] += 1
    ret = ''
    for mer in sorted(k_mer(4)):
        ret += ' {}'.format(c[mer])
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
