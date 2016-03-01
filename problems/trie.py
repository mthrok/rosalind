from __future__ import print_function


class Trie(object):
    count = 0

    def __init__(self):
        Trie.count += 1
        self.count = Trie.count
        self.edges = {}

    def insert(self, string):
        key1, key2 = string[0], string[1:]
        if key1 not in self.edges:
            self.edges[key1] = Trie()
        if key2:
            self.edges[key1].insert(key2)

    def __repr__(self):
        ret = ''
        for edge, node in self.edges.items():
            ret += '{} {} {}\n'.format(self.count, node.count, edge)
            ret += node.__repr__()
        return ret


def preprocess(string):
    return string.strip().split()


def solve(strings):
    t = Trie()
    for string in strings:
        t.insert(string)
    return t


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
