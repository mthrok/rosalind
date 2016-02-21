def preprocess(raw_data):
    strings = []
    for datum in raw_data.strip().split('>')[1:]:
        lines = datum.split('\n')
        strings.append(''.join(lines[1:]))
    return strings


def find_fixed_length_substrings(str1, str2, n):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    ret = set([])
    for iStart in range(0, len(str1)-n):
        substr = str1[iStart:iStart+n]
        if substr in str2:
            ret.add(substr)
    return ret


def solve(strings):
    if len(strings) == 0:
        return ''
    if len(strings) == 1:
        return strings[0]
    # Initialize substring set
    strings.sort(key=len, reverse=True)
    str1, str2 = strings[:2]
    max_substring_len = max(len(str1), len(str2))
    substrings = []
    for i in range(max_substring_len, 0, -1):
        substrings_ = find_fixed_length_substrings(str1, str2, i)
        substrings.extend(substrings_)
    for string in strings[2:]:
        for substring in substrings:
            if substring not in string:
                substrings.remove(substring)
    return substrings[0]


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
