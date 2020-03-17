import networkx as nx
import matplotlib.pyplot as plt



g = nx.Graph()

g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)

nx.draw(g)
plt.show()

class Graph:

    def __init__(self, vertices):
        self.V = vertices

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # Полезная функция для поиска вершины с
    # минимальное значение расстояния от множества вершин
    # еще не включено в дерево кратчайших путей

    def minDistance(self, dist, sptSet):

        # Инициализировать минимальное расстояние для следующего узла
        global min_index
        min_int = sys.maxsize
        # Поиск не ближайшей вершины не в
        # кратчайший путь

        for v in range(self.V):
            if dist[v] < min_int and sptSet[v] == False:
                min_int = dist[v]
                min_index = v
        return min_index

    # Функция, которая реализует единый источник Дейкстры
    # алгоритм кратчайшего пути для представленного графа
    # использование представления матрицы смежности

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):

            # Выберите минимальное расстояние от вершины до
            # множество вершин, еще не обработанных.
            # u всегда равен src в первой итерации

            u = self.minDistance(dist, sptSet)

            # Поместите вершину минимального расстояния в
            # дерево кратчайшего пути

            sptSet[u] = True

            # Обновить значение dist соседних вершин
            # выбранной вершины, только если текущий
            # расстояние больше нового расстояния и
            # вершина не в дереве кратчайшего пути

            for v in range(self.V):

                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


g.dijkstra()