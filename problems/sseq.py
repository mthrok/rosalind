from __future__ import print_function


def preprocess(string):
    data = string.strip().split('>')[1:]
    str1 = ''.join(data[0].split('\n')[1:])
    str2 = ''.join(data[1].split('\n')[1:])
    return str1, str2


def solve((sequence, subsequence)):
    i_query, i_search = 0, 0
    l_query, l_search = len(subsequence), len(sequence)
    indices = []
    while i_query < l_query and i_search < l_search:
        if sequence[i_search] == subsequence[i_query]:
            indices.append(i_search + 1)
            i_query += 1
        i_search += 1
    return ' '.join(map(str, indices))


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
