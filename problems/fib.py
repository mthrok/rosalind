def preprocess(string):
    return map(int, string.split(' '))


def propagate(matured_pair, unmatured_pair, k):
    new_unmatured_pair = matured_pair * k
    new_matured_pair = matured_pair + unmatured_pair
    return new_matured_pair, new_unmatured_pair


def solve((n, k)):
    matured_pair, unmatured_pair = 0, 1
    for _ in range(n-1):
        matured_pair, unmatured_pair = propagate(
            matured_pair, unmatured_pair, k)
    return matured_pair + unmatured_pair


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
