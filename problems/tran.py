from __future__ import division
from __future__ import print_function


def preprocess(string):
    data = string.strip().split('>')[1:]
    string1 = ''.join(data[0].split('\n')[1:])
    string2 = ''.join(data[1].split('\n')[1:])
    return string1, string2


def solve((str1, str2)):
    transition, transversion = 0, 0
    for c1, c2 in zip(str1, str2):
        if c1 == c2:
            continue
        pair = ''.join(sorted(c1 + c2))
        if pair in ['AG', 'CT']:
            transition += 1
        else:
            transversion += 1
    return transition / transversion


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
