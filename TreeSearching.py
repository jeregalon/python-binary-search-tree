from BinaryTree import BinaryTree
from Vertex import Vertex

def TreeSearching(T, value):
    # Si T es un vértice de un árbol
    if isinstance(T, Vertex):
        if T.root != None:
            if  value == T.root:   # si el valor buscado está en la raíz del árbol
                return True
            # si el valor es mayor, se busca en el subárbol derecho de T
            elif value > T.root:
                return TreeSearching(T.right_child, value)
            # si el valor es menor, se busca en el subárbol izquierdo de T
            else:
                return TreeSearching(T.left_child, value)
        else:
            return False
    else:
        return value == T
    
# Ejemplo:

# Construyo el árbol
mainTree = BinaryTree("OLD PROGRAMMERS NEVER DIE THEY JUST LOSE THEIR MEMORIES".split()).build()

# Probando la función
print(TreeSearching(mainTree, 'OLD'))   # 
print(TreeSearching(mainTree, 'PROGRAMMERS'))    # 
print(TreeSearching(mainTree, 'NEVER'))   # 
print(TreeSearching(mainTree, 'DIE'))   # 
print(TreeSearching(mainTree, 'THEY'))   # 
print(TreeSearching(mainTree, 'JUST'))    # 
print(TreeSearching(mainTree, 'LOSE'))   # 
print(TreeSearching(mainTree, 'THEIR'))   # 
print(TreeSearching(mainTree, 'MEMORIES'))   # 



                    

            

