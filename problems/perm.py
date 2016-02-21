def preprocess(string):
    return int(string.strip())


def perm(n):
    if n == 1:
        return [[1]]
    ret = []
    patterns = perm(n-1)
    for pattern in patterns:
        for i in range(len(pattern)+1):
            new_pattern = pattern[:i] + [n] + pattern[i:]
            ret.append(new_pattern)
    return ret


def solve(n):
    perms = perm(n)
    ret = '{}'.format(len(perms))
    for orders in perms:
        ret += '\n'
        for order in orders:
            ret += '{} '.format(order)
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
