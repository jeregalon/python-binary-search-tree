class BinaryTree:
    def __init__(self, root, left_child, righ_child):
        self._root = root
        self._left_child = left_child
        self._right_child = righ_child
    
    @property
    def root(self):
        return self._root
    
    @property
    def left_child(self):
        return self._left_child
    
    @property
    def right_child(self):
        return self._right_child
    
    @root.setter
    def root(self, value):
        self._root = value

    @left_child.setter
    def left_child(self, value):
        self._left_child = value

    @right_child.setter
    def right_child(self, value):
        self._right_child = value
    