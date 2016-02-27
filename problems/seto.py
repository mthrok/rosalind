from __future__ import print_function

import json


def preprocess(string):
    data = string.strip().split('\n')
    n = int(data[0])
    A = json.loads('[{}]'.format(data[1][1:-1]))
    B = json.loads('[{}]'.format(data[2][1:-1]))
    return n, A, B


def solve((n, A, B)):
    AcupB, AcapB = [], []
    AminusB, BminusA = [], []
    Acomp, Bcomp = [], []
    for i in range(1, n+1):
        if i in A or i in B:
            AcupB.append(i)
        if i in A and i in B:
            AcapB.append(i)
        if i in A and i not in B:
            AminusB.append(i)
        if i not in A and i in B:
            BminusA.append(i)
        if i not in A:
            Acomp.append(i)
        if i not in B:
            Bcomp.append(i)
    ret = '{{{}}}\n'.format(', '.join(map(str, AcupB)))
    ret += '{{{}}}\n'.format(', '.join(map(str, AcapB)))
    ret += '{{{}}}\n'.format(', '.join(map(str, AminusB)))
    ret += '{{{}}}\n'.format(', '.join(map(str, BminusA)))
    ret += '{{{}}}\n'.format(', '.join(map(str, Acomp)))
    ret += '{{{}}}\n'.format(', '.join(map(str, Bcomp)))
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
