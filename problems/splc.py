from __future__ import print_function

from common import dna2rna
from common import rna2prot


def preprocess(string):
    strings = []
    for chunk in string.strip().split('>')[1:]:
        strings.append(''.join(chunk.split('\n')[1:]))
    return strings


def del_exon(base, exon):
    l_exon = len(exon)
    while True:
        changed = False
        for i in range(len(base)-l_exon):
            if base[i:i+l_exon] == exon:
                base = base[:i] + base[i+l_exon:]
                changed = True
                break
        if not changed:
            break
    return base


def solve(strings):
    base = dna2rna(strings[0])
    exons = map(dna2rna, strings[1:])
    for exon in exons:
        base = del_exon(base, exon)
    return rna2prot(base)


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
