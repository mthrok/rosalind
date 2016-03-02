from __future__ import division
from __future__ import print_function


def preprocess(raw_data):
    data = raw_data.strip().split('\n')
    N, x = data[0].split(' ')
    string = data[1]
    return int(N), float(x), string


def solve((N, x, string)):
    base_prob = {
        'A': (1-x) / 2,
        'C': x / 2,
        'T': (1-x) / 2,
        'G': x / 2,
    }
    prob = 1 - reduce(lambda p, c: p * base_prob[c], string, 1)
    return 1 - prob ** N


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
