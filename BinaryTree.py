from Vertex import Vertex

class BinaryTree:
    def __init__(self, elements):
        self._elements = elements
        self._root = Vertex(None, None, None)

    def build(self):
        elements = sorted(self._elements)
        leftSubtree = []
        rightSubtree = []
        leng = len(elements)
        if leng > 2:
            if leng % 2 == 0:
                half = int(leng / 2) - 1
            else:
                half = leng // 2
            leftSubtree = BinaryTree(elements[:half])
            root = elements[half]
            rightSubtree = BinaryTree(elements[half+1:])
        elif leng == 2:
            root = elements[0]
            leftSubtree = BinaryTree([])
            rightSubtree = BinaryTree([elements[1]])
        elif leng == 1:
            root = elements[0]
            leftSubtree = BinaryTree([])
            rightSubtree = BinaryTree([])
        else:
            root = None

        newVertex = Vertex(root, None, None)
        if leng != 0:
            newVertex.left_child = leftSubtree.build()
            newVertex.right_child = rightSubtree.build()
        
        return newVertex

