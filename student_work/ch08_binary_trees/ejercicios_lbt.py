from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si T es un árbol binario completo."""
    if T.is_empty():
        return True

    cola = [T.root()]
    se_encontro_un_hueco = False

    while cola:
        posicion = cola.pop(0)

        hijo_izquierdo = T.left(posicion)
        hijo_derecho = T.right(posicion)
        hijos = [hijo_izquierdo, hijo_derecho]

        for hijo in hijos:
            if hijo is None:
                se_encontro_un_hueco = True
            elif se_encontro_un_hueco:
                return False
            else:
                cola.append(hijo)
    return True
def camino(T, p, q):
    """Retorna los elementos del camino de p a q, separados por ' -> '."""

    ancestros_de_p = []
    posicion = p
    while posicion is not None:
        ancestros_de_p.append(posicion)
        posicion = T.parent(posicion)
    ruta_desde_q = []
    posicion = q

    while posicion not in ancestros_de_p:
        ruta_desde_q.append(posicion)
        posicion = T.parent(posicion)
    ancestro_comun = posicion
    ruta = []
    for ancestro in ancestros_de_p:
        ruta.append(ancestro)
        if ancestro == ancestro_comun:
            break


    ruta_desde_q.reverse()
    ruta.extend(ruta_desde_q)

    elementos = [str(posicion.element()) for posicion in ruta]
    return " -> ".join(elementos)
