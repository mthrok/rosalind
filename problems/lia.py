from __future__ import print_function
from collections import Counter


def preprocess(string):
    return list(map(int, string.strip().split(' ')))


def mate(gene1, gene2=('Aa', 'Bb')):
    new_gene_set = Counter()
    for i in range(4):
        i1, i2 = i % 2, i // 2
        for j in range(4):
            j1, j2 = j % 2, j // 2
            new_g1 = ''.join(sorted([gene1[0][i1], gene2[0][j1]]))
            new_g2 = ''.join(sorted([gene1[1][i2], gene2[1][j2]]))
            new_gene = (new_g1, new_g2)
            new_gene_set[new_gene] += 1
    return new_gene_set


def solve((k, N)):
    for gene1 in ['AA', 'Aa', 'aa']:
        for gene2 in ['BB', 'Bb', 'bb']:
            gene = (gene1, gene2)
            new_gene = mate(gene)
            print(gene, ('Aa', 'Bb'))
            for key, count in new_gene.items():
                print(key, count)
            print()
    return None


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
