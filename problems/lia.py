from __future__ import print_function
from __future__ import division

from collections import Counter

import numpy as np


def preprocess(string):
    return list(map(int, string.strip().split(' ')))


def print_transition_matrix(mat, labels):
    print(' ' * 6, end='')
    for label in labels:
        print('{:<6}'.format(label), end=' ')
    print()
    for r in range(9):
        print(labels[r], end=': ')
        for c in range(9):
            print('{:.4f}'.format(mat[r, c]), end=' ')
        print()


def mate(gene1, gene2='AaBb'):
    """Compute the probability distribution of the offspring genes"""
    dist = Counter()
    for i in range(4):
        i1, i2 = i % 2, 2 + i // 2
        for j in range(4):
            j1, j2 = j % 2, 2 + j // 2
            gene = '{}{}'.format(
                ''.join(sorted([gene1[i1], gene2[j1]])),
                ''.join(sorted([gene1[i2], gene2[j2]])))
            dist[gene] += 1 / 16
    return dist


def construct_base_transition_matrix():
    """Compute the transition matrix of population for 1 generation"""
    T = np.zeros((9, 9))
    labels = ['AABB', 'AABb', 'AAbb', 'AaBB',
              'AaBb', 'Aabb', 'aaBB', 'aaBb', 'aabb']
    for g1 in ['AA', 'Aa', 'aa']:
        for g2 in ['BB', 'Bb', 'bb']:
            parent_gene = '{}{}'.format(g1, g2)
            dist = mate(parent_gene)
            raw = labels.index(parent_gene)
            for offspring_gene, prob in dist.items():
                col = labels.index(offspring_gene)
                T[raw, col] = prob
    return T, labels


def construct_transition_matrix(k):
    """Compute the transition matrix of population for k generation"""
    T, labels = construct_base_transition_matrix()
    mat = np.eye(9)
    for _ in range(k):
        mat = np.dot(mat, T)
    return mat, labels


def factorial(N):
    ret = 1
    for i in range(N):
        ret *= (i+1)
    return ret


def prob_N(p, n, r):
    """Compute the probability that event P occurs exactly r times.

    p^r * (1-p)^(n-r) * n! / r! / (n-r)! """
    q, m = 1 - p, n - r
    return (p ** r) * (q ** m) * factorial(n) / factorial(r) / factorial(m)


def solve((k, N)):
    T, _ = construct_transition_matrix(k)
    dist = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0]])
    dist = np.dot(dist, T)
    ret = 0.0
    for n in range(N, 2**k + 1):
        ret += prob_N(dist[0][4], 2**k, n)
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
