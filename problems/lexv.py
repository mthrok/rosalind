from __future__ import print_function


def preprocess(string):
    data = string.strip().split('\n')
    alphabets = data[0].split(' ')
    n = int(data[1])
    return alphabets, n


def solve((alphabets, n)):
    n_alphabets = len(alphabets)
    substrings = []
    indices = [i for i in range(n_alphabets)]
    for length in range(1, n+1):
        for substring_index in range(n_alphabets ** length):
            substring = []
            for _ in range(length):
                substring.append(indices[substring_index % n_alphabets])
                substring_index //= n_alphabets
            substrings.append(substring)
    substrings.sort()
    ret = []
    for substring in substrings:
        string = ''.join(map(lambda x: alphabets[x], substring))
        ret.append(string)
    return '\n'.join(ret)


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
