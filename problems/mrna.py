from common import REVERSE_RNA_CODON


def preprocess(string):
    return string.strip()


def solve(string):
    # Convert REVERSE_RNA_CODON table to counts
    codon = {key: len(value) for key, value in REVERSE_RNA_CODON.items()}
    ret = 3  # For 'Stop'
    for char in string:
        ret *= codon[char]
        if ret > 1000000:
            ret %= 1000000
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
