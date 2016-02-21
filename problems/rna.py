from __future__ import print_function

import time


def solve(string):
    return string.replace('T', 'U')


def preprocess(string):
    return string.strip()


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
