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

mainTree = BinaryTree('FOUR', None, None)
andT = BinaryTree('AND', None, None)
scoreT = BinaryTree('SCORE', None, None)
agoT = BinaryTree('AGO', None, None)
sevenT = BinaryTree('SEVEN', None, None)
ourT = BinaryTree('OUR', None, None)
yearsT = BinaryTree('YEARS', None, None)
broughtT = BinaryTree('BROUGHT', None, None)
forefathersT = BinaryTree('FOREFATHERS', None, None)
forthT = BinaryTree('FORTH', None, None)

broughtT.right_child = forthT
ourT.left_child = broughtT
agoT.right_child = ourT
andT.left_child = agoT
mainTree.left_child = andT

yearsT.left_child = forefathersT
sevenT.right_child = yearsT
scoreT.right_child = sevenT
mainTree.right_child = scoreT

# Probando la función

print(TreeSearching(mainTree, 'FOREFATHERS'))   # True
print(TreeSearching(mainTree, 'FOREFATHER'))    # False
print(TreeSearching(mainTree, 'AND'))   # True
print(TreeSearching(mainTree, 'BRO'))   # False
print(TreeSearching(mainTree, 7))       # False



                    

            

