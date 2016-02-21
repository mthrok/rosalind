from common import RNA_CODON


def preprocess(string):
    return string.strip()


def solve(string):
    ret = ''
    for i in range(0, len(string), 3):
        substr = string[i:i+3]
        if RNA_CODON[substr] == 'Stop':
            break
        ret += RNA_CODON[substr]
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
    print('Input:\n{}'.format(data))
    ret = solve(data)
    print('Output:\n{}'.format(ret))


if __name__ == '__main__':
    main()
