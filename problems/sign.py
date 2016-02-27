from __future__ import print_function


def preprocess(string):
    return int(string.strip())


def factorial(n):
    ret = 1
    for i in range(2, n+1):
        ret *= i
    return ret


def permutation(n):
    if n == 1:
        return [[1]]
    base_perms = permutation(n-1)
    ret = []
    for i in range(0, n):
        for base_perm in base_perms:
            perm = base_perm[:i] + [n] + base_perm[i:]
            ret.append(perm)
    return ret


def assign_sign(pattern):
    l_pattern = len(pattern)
    ret = []
    for i_sign in range(2 ** l_pattern):
        new_pattern = []
        for ind in range(l_pattern):
            val = pattern[ind]
            if i_sign % 2:
                val *= -1
            new_pattern.append(val)
            i_sign //= 2
        ret.append(new_pattern)
    return ret


def assign_signs(patterns):
    ret = []
    for pattern in patterns:
        ret.extend(assign_sign(pattern))
    return ret


def solve(n):
    len_ans = factorial(n) * (2 ** n)
    perms = permutation(n)
    perms = assign_signs(perms)
    assert len_ans == len(perms)
    ret = '{}'.format(len_ans)
    for perm in perms:
        ret += '\n{}'.format(' '.join(map(str, perm)))
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
