def preprocess(string):
    return map(int, string.split(' '))


def propagate(pairs):
    new_pairs = sum(pairs[1:])
    return [new_pairs] + pairs[:-1]


def solve((n, m)):
    pairs = [1] + [0] * (m - 1)
    for _ in range(n - 1):
        pairs = propagate(pairs)
    return sum(pairs)


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
