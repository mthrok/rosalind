def preprocess(string):
    data = string.strip().split('\n')
    symbols = data[0].split(' ')
    n = int(data[1])
    return symbols, n


def solve((symbols, n)):
    l_symbols = len(symbols)
    n_ans = l_symbols ** n
    ret = []
    for ind in range(n_ans):
        ans = ''
        for _ in range(n):
            ans = symbols[ind % l_symbols] + ans
            ind = ind // l_symbols
        ret.append(ans)
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
