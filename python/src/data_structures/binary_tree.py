class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        lines = self._build_tree_string(self.root, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def _build_tree_string(self, root, curr_index, include_index=False, delimiter='-'):
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
        else:
            node_repr = str(root.value)

        new_root_width = gap_size = len(node_repr)

        # Recursively build left and right subtrees
        l_box, l_box_width, l_root_start, l_root_end = self._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = self._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)

        # Draw the branch connecting the current root node to left sub-tree
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
            gap_size += 1

        # Print the current root node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to right sub-tree
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
            gap_size += 1

        # Combine left and right sub-trees
        gap = ' ' * gap_size
        new_box = [''.join(line1), ''.join(line2)]

        # Merge the sub-boxes into one
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), l_box_width + gap_size // 2, l_box_width + gap_size // 2 + new_root_width

    def add(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if current.value > value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
        return self
    
arvore = Tree()

arvore.add(3)
arvore.add(2)
arvore.add(0)
arvore.add(7)
arvore.add(6)
arvore.add(8)
arvore.add(2)
arvore.add(7)
arvore.add(9)

print(arvore)