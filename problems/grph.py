from collections import defaultdict


def preprocess(string):
    return string.strip()


def solve(data):
    prefixes = defaultdict(list)
    suffixes = defaultdict(list)
    for datum in data.split('>')[1:]:
        lines = datum.split('\n')
        label = lines[0]
        string = ''.join(lines[1:])
        prefixes[string[:3]].append(label)
        suffixes[string[-3:]].append(label)
    common_keys = set(prefixes.keys()) | set(suffixes.keys())
    ret = ''
    for key in common_keys:
        for l1 in suffixes[key]:
            for l2 in prefixes[key]:
                if not l1 == l2:
                    ret = ret + '{} {}\n'.format(l1, l2)
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
    print('INPUT:\n{}\n'.format(data))
    ret = solve(data)
    print('OUTPUT:\n{}'.format(ret))


if __name__ == '__main__':
    main()
