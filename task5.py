# Візуалізація обходів бінарного дерева (DFS і BFS) з кольорами

import uuid
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

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Додає ребра та позиції для вузлів графа.
    
    Параметри:
        graph (nx.DiGraph): Граф для візуалізації.
        node (Node): Поточний вузол.
        pos (dict): Словник позицій вузлів.
        x, y (float): Координати поточного вузла.
        layer (int): Рівень у дереві.
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

def draw_tree(tree_root, title, filename):
    """
    Візуалізує дерево та зберігає у файл PNG.
    
    Параметри:
        tree_root (Node): Корінь дерева.
        title (str): Заголовок малюнка.
        filename (str): Ім'я вихідного файлу.
    """
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.savefig(filename, format="png", bbox_inches="tight")
    plt.close()

def dfs_iterative(root):
    """
    Виконує ітеративний обхід у глибину (DFS) із зміною кольорів.
    
    Параметри:
        root (Node): Корінь дерева.
    
    Повертає:
        dict: Мапа вузлів і їхніх кольорів.
    """
    if not root:
        return {}
    
    colors = {}
    stack = []  # Стек для ітеративного DFS
    visited = set()
    visit_order = 0
    total_nodes = 0
    
    # Підрахунок загальної кількості вузлів
    def count_nodes(node):
        nonlocal total_nodes
        if node:
            total_nodes += 1
            count_nodes(node.left)
            count_nodes(node.right)
    
    count_nodes(root)
    
    # Ініціалізація стеку з коренем
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left  # Спочатку йдемо вліво
        
        current = stack.pop()
        if current.id not in visited:
            visited.add(current.id)
            visit_order += 1
            
            # Обчислюємо колір на основі порядку відвідування
            r = int("1A", 16) + int((255 - 26) * (visit_order - 1) / total_nodes)
            g = int("2B", 16) + int((238 - 43) * (visit_order - 1) / total_nodes)
            b = int("3C", 16) + int((255 - 60) * (visit_order - 1) / total_nodes)
            color = f"#{r:02x}{g:02x}{b:02x}"
            colors[current.id] = color
            
        current = current.right  # Переходимо вправо
    
    return colors

def bfs_iterative(root):
    """
    Виконує ітеративний обхід у ширину (BFS) із зміною кольорів.
    
    Параметри:
        root (Node): Корінь дерева.
    
    Повертає:
        dict: Мапа вузлів і їхніх кольорів.
    """
    if not root:
        return {}
    
    colors = {}
    queue = []  # Черга для ітеративного BFS
    visited = set()
    visit_order = 0
    total_nodes = 0
    
    # Підрахунок загальної кількості вузлів
    def count_nodes(node):
        nonlocal total_nodes
        if node:
            total_nodes += 1
            count_nodes(node.left)
            count_nodes(node.right)
    
    count_nodes(root)
    
    # Ініціалізація черги з коренем
    queue.append(root)
    while queue:
        current = queue.pop(0)  # Вилучаємо перший елемент
        if current.id not in visited:
            visited.add(current.id)
            visit_order += 1
            
            # Обчислюємо колір на основі порядку відвідування
            r = int("1A", 16) + int((255 - 26) * (visit_order - 1) / total_nodes)
            g = int("2B", 16) + int((238 - 43) * (visit_order - 1) / total_nodes)
            b = int("3C", 16) + int((255 - 60) * (visit_order - 1) / total_nodes)
            color = f"#{r:02x}{g:02x}{b:02x}"
            colors[current.id] = color
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    return colors

def main():
    """Створює дерево та візуалізує обходи DFS і BFS."""
    # Створюємо дерево
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    
    # Виконуємо DFS і оновлюємо кольори
    dfs_colors = dfs_iterative(root)
    for node_id, color in dfs_colors.items():
        for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left]:
            if node.id == node_id:
                node.color = color
    
    # Візуалізуємо DFS
    draw_tree(root, "Обхід у глибину (DFS)", "dfs_traversal.png")
    
    # Скидаємо кольори для BFS
    for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left]:
        node.color = "skyblue"
    
    # Виконуємо BFS і оновлюємо кольори
    bfs_colors = bfs_iterative(root)
    for node_id, color in bfs_colors.items():
        for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left]:
            if node.id == node_id:
                node.color = color
    
    # Візуалізуємо BFS
    draw_tree(root, "Обхід у ширину (BFS)", "bfs_traversal.png")

if __name__ == "__main__":
    main()