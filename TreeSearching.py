from BinaryTree import BinaryTree

def TreeSearching(T, value):
    # si T es un árbol binario:
    if isinstance(T, BinaryTree):
        if  value == T.root:   # si el valor buscado está en la raíz del árbol
            return True
        # si el valor no se encuentra en la raíz del árbol, se busca en uno de sus dos hijos
        else:
            return TreeSearching(T.left_child, value) or TreeSearching(T.right_child, value)
    else:
        return value == T
    
# Ejemplo:

# Construyo el árbol
mainTree = BinaryTree("OLD PROGRAMMERS NEVER DIE, THEY JUST LOSE THEIR MEMORIES".split())

# Probando la función
print(TreeSearching(mainTree, 'FOREFATHERS'))   # 
print(TreeSearching(mainTree, 'PROGRAMMERS'))    # 
print(TreeSearching(mainTree, 'AND'))   # 
print(TreeSearching(mainTree, 'DIE'))   # 
print(TreeSearching(mainTree, 7))       # 



                    

            

