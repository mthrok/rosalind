from __future__ import print_function


def preprocess(string):
    lines = string.strip().split('\n')
    n = int(lines[0])
    edges = [list(map(int, line.split(' '))) for line in lines[1:]]
    return n, edges


def merge_node_sets(node_sets):
    changed = True
    while changed:
        changed = False
        n_sets = len(node_sets)
        for i in range(n_sets):
            for j in range(i+1, n_sets):
                if node_sets[i] & node_sets[j]:
                    node_sets[i] = node_sets[i] | node_sets[j]
                    del node_sets[j]
                    changed = True
                    break
            if changed:
                break


def divide_edges(edges):
    node_sets = []
    for node1, node2 in edges:
        for node_set in node_sets:
            if node1 in node_set or node2 in node_set:
                node_set.update([node1, node2])
                break
        else:
            node_sets.append(set([node1, node2]))
    merge_node_sets(node_sets)
    return node_sets


def append_node(node_sets, i):
    for node_set in node_sets:
        if i in node_set:
            return
    node_sets.append(set([i]))


def solve((n, edges)):
    ret = divide_edges(edges)
    for i in range(n):
        append_node(ret, i+1)
    return len(ret) - 1


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
