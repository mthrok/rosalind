def preprocess(string):
    chunk = string.strip().split('>')[1]
    return ''.join(chunk.split('\n')[1:])


def reverse_complement(string):
    code = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    return ''.join(map(lambda c: code[c], string[::-1]))


def find_rev_pal(string, min_len=4, max_len=12):
    ret = []
    min_len = max(min_len, 2)
    max_len = min(max_len+1, len(string)+1)
    for length in range(min_len, max_len):
        sub_str1 = string[:length]
        sub_str2 = reverse_complement(sub_str1)
        if sub_str1 == sub_str2:
            ret.append(length)
    return ret


def solve(string):
    palindromes = []
    for i in range(len(string)):
        lengths = find_rev_pal(string[i:], min_len=4, max_len=12)
        for length in lengths:
            palindromes.append((i+1, length))
    ret = ''
    for p in palindromes:
        ret += '{} {}\n'.format(*p)
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
