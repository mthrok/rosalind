from __future__ import print_function


def LIS(seq):
    increasing = []
    for i in range(len(seq)):
        increasing_ = [seq[i]]
        for j in range(i):
            if (increasing[j][-1] < seq[i] and
                len(increasing[j]) + 1 > len(increasing_)):
                increasing_ = increasing[j] + [seq[i]]
        increasing.append(increasing_)
    longest = increasing[0]
    for i in range(1, len(increasing)):
        if len(increasing[i]) > len(longest):
            longest = increasing[i]
    return longest


def LDS(seq):
    decreasing = []
    for i in range(len(seq)):
        decreasing_ = [seq[i]]
        for j in range(i):
            if (decreasing[j][-1] > seq[i] and
                len(decreasing[j]) + 1 > len(decreasing_)):
                decreasing_ = decreasing[j] + [seq[i]]
        decreasing.append(decreasing_)
    longest = decreasing[0]
    for i in range(1, len(decreasing)):
        if len(decreasing[i]) > len(longest):
            longest = decreasing[i]
    return longest


def solve((n, perm)):
    lis = LIS(perm)
    lds = LDS(perm)
    return '{}\n{}\n'.format(' '.join(map(str, lis)), ' '.join(map(str, lds)))


def preprocess(string):
    data = string.strip().split('\n')
    n = int(data[0])
    perm = list(map(int, data[1].split(' ')))
    return n, perm


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
