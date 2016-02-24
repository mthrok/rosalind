from __future__ import print_function

from common import RNA_CODON


def preprocess(string):
    return ''.join(string.strip().split('>')[1].split('\n')[1:])


def dna2rna(string):
    return string.replace('T', 'U')


def reverse_complement(string):
    code = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return ''.join(map(lambda c: code[c], string[::-1]))


def findSpecialCodons(string):
    starts, ends = [], []
    for i in range(len(string)):
        substr = string[i:i+3]
        if substr == 'AUG':
            starts.append(i)
        if substr in ['UAA', 'UAG', 'UGA']:
            ends.append(i)
    return starts, ends


def rna2prot(string):
    ret = ''
    for i in range(0, len(string), 3):
        substr = string[i:i+3]
        if RNA_CODON[substr] == 'Stop':
            break
        ret += RNA_CODON[substr]
    return ret


def find_orf(string):
    starts, ends = findSpecialCodons(string)
    ret = set()
    for start in starts:
        for end in ends:
            if start >= end:
                continue
            if (end - start) % 3 != 0:
                continue
            substr = string[start:end+3]
            ret.add(rna2prot(substr))
    return ret


def solve(string):
    prots = set()
    prots.update(find_orf(dna2rna(string)))
    prots.update(find_orf(dna2rna(reverse_complement(string))))
    return '\n'.join(prots)


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
