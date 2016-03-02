from __future__ import division
from __future__ import print_function


def preprocess(string):
    return ''.join(string.strip().split('>')[1].split('\n')[1:])


def perm(n, k):
    ret = 1
    for i in range(k):
        ret *= n - i
    return ret


def solve(string):
    char_set = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
    for char in string:
        char_set[char] += 1
    n1 = max(char_set['A'], char_set['U'])
    k1 = min(char_set['A'], char_set['U'])
    n2 = max(char_set['C'], char_set['G'])
    k2 = min(char_set['C'], char_set['G'])
    return perm(n1, k1) * perm(n2, k2)


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
