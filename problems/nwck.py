from __future__ import print_function


class Node(object):
    def __init__(self, value=''):
        self.value = value
        self.children = []

    def append(self, node):
        self.children.append(node)

    def depth(self, value):
        if self.value == value:
            return 0
        for child in self.children:
            d = child.depth(value)
            if d > -1:
                return d + 1
        return -1

    def __repr__(self):
        value = self.value if self.value else None
        if self.children:
            ret = '{} -> {}'.format(value, self.children)
        else:
            ret = '{}'.format(value)
        return ret

    def __contains__(self, value):
        if self.value == value:
            return True
        for child in self.children:
            if value in child:
                return True
        return False


def constructTree(newick, indent=0):
    assert newick.count('(') == newick.count(')')
    if newick.startswith('('):
        iClose = newick.rfind(')')
        ret = Node(newick[iClose+1:])
        brackets = 0
        iStart = 1
        for i in range(1, iClose):
            c = newick[i]
            if c == '(':
                brackets += 1
            if c == ')':
                brackets -= 1
            if c == ',':
                if brackets == 0:
                    ret.append(constructTree(newick[iStart:i], indent+1))
                    iStart = i+1
        ret.append(constructTree(newick[iStart:iClose], indent+1))
        # print('{} INPUT:{}'.format('*'*indent, newick))
        # print('{}OUTPUT:{}'.format('*'*indent, ret))
    else:
        ret = Node(newick)
    return ret


def traverse(root, val1, val2):
    assert val1 in root
    assert val2 in root
    if root.value == val1:
        return root.depth(val2)
    if root.value == val2:
        return root.depth(val1)
    depth1, depth2 = -1, -1
    for child in root.children:
        in1, in2 = val1 in child, val2 in child
        if in1 and in2:
            return traverse(child, val1, val2)
        if in1:
            depth1 = child.depth(val1) + 1
        if in2:
            depth2 = child.depth(val2) + 1
    return depth1 + depth2


def preprocess(raw_data):
    lines = raw_data.strip().split('\n')
    ret = []
    for i in range(0, len(lines), 3):
        newick = lines[i][:-1]
        x, y = lines[i+1].split(' ')
        ret.append((newick, x, y))
    return ret


def solve(data):
    ret = []
    for newick, x, y in data:
        # print('='*79)
        # print('{}\n\n{}\n{}\n\n'.format(newick, x, y))
        tree = constructTree(newick)
        ret.append(traverse(tree, x, y))
    return ' '.join(map(str, ret))


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
