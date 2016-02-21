from __future__ import division


def preprocess(string):
    return string.strip()


def parse_string(string):
    ret = {}
    current_key = None
    for line in string.split('\n'):
        if line.startswith('>'):
            current_key = line[1:]
            ret[current_key] = ''
        else:
            ret[current_key] += line
    return ret


def comp_gc(string):
    gc = 0
    for c in string:
        if c in 'GC':
            gc += 1
    return 100 * gc / len(string)


def solve(string):
    data = parse_string(string)
    best_ratio = 0.0
    best_key = None
    for key, value in data.items():
        ratio = comp_gc(value)
        if ratio > best_ratio:
            best_ratio = ratio
            best_key = key
    return '{}\n{}'.format(best_key, best_ratio)


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
