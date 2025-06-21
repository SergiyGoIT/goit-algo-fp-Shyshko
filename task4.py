# Реалізація візуалізації бінарної купи на основі бінарного дерева

import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        """Ініціалізує вузол дерева."""
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def heap_to_tree(heap, index=0):
    """
    Перетворює масив бінарної купи в бінарне дерево.
    
    Параметри:
        heap (list): Масив, що представляє бінарну купу.
        index (int): Поточний індекс у масиві.
    
    Повертає:
        Node: Корінь піддерева або None.
    """
    if index >= len(heap):
        return None
    
    node = Node(heap[index])
    
    # Лівий нащадок: 2*index + 1
    node.left = heap_to_tree(heap, 2 * index + 1)
    # Правий нащадок: 2*index + 2
    node.right = heap_to_tree(heap, 2 * index + 2)
    
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає ребра та позиції для вузлів графа.
    
    Параметри:
        graph (nx.DiGraph): Граф для візуалізації.
        node (Node): Поточний вузол.
        pos (dict): Словник позицій вузлів.
        x, y (float): Координати поточного вузла.
        layer (int): Рівень у дереві.
    
    Повертає:
        nx.DiGraph: Оновлений граф.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(tree_root):
    """
    Візуалізує бінарну купу як дерево та зберігає у файл PNG.
    
    Параметри:
        tree_root (Node): Корінь дерева купи.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title("Візуалізація бінарної купи")
    plt.savefig("heap_visualization.png", format="png", bbox_inches="tight")
    plt.close()  # Закриваємо фігуру, щоб уникнути відображення в Codespaces

def main():
    """Створює бінарну купу та візуалізує її."""
    # Приклад масиву для створення min-heap
    numbers = [0, 1, 3, 4, 5, 10]
    
    # Створюємо min-heap
    heapq.heapify(numbers)
    print("Масив після heapify:", numbers)
    
    # Перетворюємо купу в дерево
    root = heap_to_tree(numbers)
    
    # Візуалізуємо купу
    draw_heap(root)

if __name__ == "__main__":
    main()