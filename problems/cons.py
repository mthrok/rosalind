def preprocess(string):
    return string.strip()


class Profile(object):
    def __init__(self):
        self.counts = {
            'A': [],
            'C': [],
            'G': [],
            'T': [],
        }
        self.length = 0

    def extend(self, length):
        while self.length < length:
            for l in self.counts.values():
                l.append(0)
            self.length += 1

    def add(self, key, index, value=1):
        if self.length <= index:
            self.extend(index+1)
        self.counts[key][index] += value

    def consensus(self):
        ret = ''
        for i in range(self.length):
            max_count = -1
            max_key = None
            for key in self.counts.keys():
                if self.counts[key][i] > max_count:
                    max_count = self.counts[key][i]
                    max_key = key
            ret += max_key
        return ret


def solve(string):
    profile = Profile()
    for chunk in string.split('>')[1:]:
        index = 0
        for line in chunk.strip().split('\n'):
            for char in line:
                if char not in 'AGCT':
                    continue
                profile.add(char, index)
                index += 1
    ret = '{}'.format(profile.consensus())
    for char in 'ACGT':
        ret += '\n{}: {}'.format(
            char, ' '.join(map(str, profile.counts[char])))
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
    print('Input:\n{}'.format(data))
    ret = solve(data)
    print('Output:\n{}'.format(ret))


if __name__ == '__main__':
    main()
