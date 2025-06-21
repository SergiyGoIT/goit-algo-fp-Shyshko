# Реалізація алгоритму Дейкстри з використанням бінарної купи для зваженого графа

import heapq
from collections import defaultdict
import math

class Graph:
    def __init__(self):
        """Ініціалізує граф як список суміжності."""
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        """Додає ребро з вагою між вершинами u і v."""
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Для неорієнтованого графа

    def dijkstra(self, start):
        """
        Реалізує алгоритм Дейкстри для знаходження найкоротших шляхів.
        
        Параметри:
            start: Початкова вершина.
        
        Повертає:
            distances: Словник із найкоротшими відстанями до кожної вершини.
            predecessors: Словник із попередниками для відновлення шляхів.
        """
        # Ініціалізація відстаней і попередників
        distances = {vertex: math.inf for vertex in self.graph}
        distances[start] = 0
        predecessors = {vertex: None for vertex in self.graph}
        
        # Бінарна купа для вибору вершини з мінімальною відстанню
        pq = [(0, start)]  # (відстань, вершина)
        visited = set()
        
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)
            
            # Якщо вершина вже оброблена, пропускаємо
            if current_vertex in visited:
                continue
                
            visited.add(current_vertex)
            
            # Переглядаємо всіх сусідів поточної вершини
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor in visited:
                    continue
                    
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях, оновлюємо відстань
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, predecessors

    def get_path(self, predecessors, end):
        """Відновлює шлях від початкової вершини до кінцевої за попередниками."""
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors[current]
        return path[::-1]  # Перевертаємо шлях

def main():
    """Приклад використання алгоритму Дейкстри."""
    # Створюємо граф
    g = Graph()
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
    ]
    
    for u, v, weight in edges:
        g.add_edge(u, v, weight)
    
    # Запускаємо алгоритм Дейкстри від вершини 'A'
    start_vertex = 'A'
    distances, predecessors = g.dijkstra(start_vertex)
    
    # Виводимо результати
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        if distance == math.inf:
            print(f"До {vertex}: недосяжно")
        else:
            path = g.get_path(predecessors, vertex)
            print(f"До {vertex}: {distance}, шлях: {' -> '.join(path)}")

if __name__ == "__main__":
    main()