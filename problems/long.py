from __future__ import division
from __future__ import print_function

import numpy as np


def preprocess(raw_data):
    data = raw_data.strip().split('>')[1:]
    return [''.join(datum.split('\n')[1:]) for datum in data]


def remove_contained(strings):
    def remove_one_string(strings):
        n_strings = len(strings)
        for i in range(n_strings):
            for j in range(i+1, n_strings):
                str1, str2 = strings[i], strings[j]
                if str1.startswith(str2):
                    del strings[j]
                    return True
                if str2.startswith(str1):
                    del strings[i]
                    return True
        return False
    changed = True
    while changed:
        changed = remove_one_string(strings)


def common_substring(string1, string2):
    min_len = min(len(string1), len(string2))
    for l in range(min_len, min_len//2-1, -1):
        if string1[-l:] == string2[:l]:
            return l
    return 0


def construct_connection_matrix(strings):
    n_strings = len(strings)
    con = np.zeros((n_strings, n_strings), dtype=np.int)
    for i in range(n_strings):
        for j in range(i+1, n_strings):
            con[i, j] = common_substring(strings[i], strings[j])
            con[j, i] = common_substring(strings[j], strings[i])
    return con


def reconstruct_connection(con, path):
    last = path[-1]
    if np.sum(con[last]) == 0:
        return path
    for i, common in enumerate(con[last]):
        if i in path:
            continue
        if common > 0:
            new_path = reconstruct_connection(con, path + [i])
            if new_path:
                return new_path
    return []


def retrieve_path(con):
    start = np.nonzero(np.sum(con, axis=0) == 0)[0][0]
    return reconstruct_connection(con, [start])


def reconstruct_superstring(strings, con, path):
    ret = strings[path[0]]
    for i1, i2 in zip(path[:-1], path[1:]):
        ret += strings[i2][con[i1, i2]:]
    return ret


def solve(strings):
    remove_contained(strings)
    con = construct_connection_matrix(strings)
    path = retrieve_path(con)
    ret = reconstruct_superstring(strings, con, path)
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
