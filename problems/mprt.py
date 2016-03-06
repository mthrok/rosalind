from __future__ import print_function

import re
import time
import urllib2


def find_motif(seq, pattern):
    ret = []
    for i in range(len(seq)):
        if re.match(pattern, seq[i:i+4]):
            ret.append(i+1)
    return ret


def solve(protain_data):
    indices_set = []
    for uniprot_id, sequence in protain_data:
        indices = find_motif(sequence, r'N[^P][ST][^P]')
        if indices:
            indices_set.append((uniprot_id, indices))
    ret = ''
    for uniprot_id, indices in indices_set:
        ret += '{}\n{}\n'.format(uniprot_id, ' '.join(map(str, indices)))
    return ret


def preprocess(string):
    ret = []
    for uniprot_id in string.strip().split('\n'):
        url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot_id)
        print('Fetching: {}'.format(url))
        raw_data = urllib2.urlopen(url).read()
        data = ''.join(raw_data.strip().split('\n')[1:])
        ret.append((uniprot_id, data))
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
    t0 = time.time()
    ret = solve(data)
    t1 = time.time()
    print('*TIME*\n{} [sec]\n'.format(t1-t0))
    print('*OUTPUT*\n{}'.format(ret))


if __name__ == '__main__':
    main()
