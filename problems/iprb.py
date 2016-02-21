from __future__ import division


def preprocess(string):
    return list(map(int, string.strip().split(' ')))


def solve((k, m, n)):
    s = k + m + n
    a = m * (m - 1) / (s * (s - 1))
    b = n * (n - 1) / (s * (s - 1))
    c = m * n / (s * (s - 1))
    return 1 - a / 4 - b - c


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
    print('Input:\n{}'.format(data))
    ret = solve(data)
    print('Output:\n{}'.format(ret))


if __name__ == '__main__':
    main()
