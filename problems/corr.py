from __future__ import print_function

from collections import defaultdict


def preprocess(raw_data):
    strings = []
    for chunk in raw_data.strip().split('>')[1:]:
        strings.append(''.join(chunk.split('\n')[1:]))
    return strings


def rev_comp(string):
    convert = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }
    ret = ''
    for char in string:
        ret = convert[char] + ret
    return ret


def divide_strings(strings):
    indices = defaultdict(list)
    for i, string in enumerate(strings):
        rev_str = rev_comp(string)
        if rev_str in indices:
            indices[rev_str].append(i)
        else:
            indices[string].append(i)
    corrects, incorrects = set(), set()
    for index_set in indices.values():
        if len(index_set) >= 2:
            for index in index_set:
                corrects.add(strings[index])
                corrects.add(rev_comp(strings[index]))
        else:
            for index in index_set:
                incorrects.add(strings[index])
    return corrects, incorrects


def dist(str1, str2):
    ret = 0
    for c1, c2 in zip(str1, str2):
        if not c1 == c2:
            ret += 1
    return ret


def solve(strings):
    corrects, incorrects = divide_strings(strings)
    ret = ''
    for incorrect in incorrects:
        for correct in corrects:
            if dist(correct, incorrect) == 1:
                ret += '{}->{}\n'.format(incorrect, correct)
                break
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
