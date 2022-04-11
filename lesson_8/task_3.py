"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""


def gen_graph(count_vertex: int):

    graph = {j: [i for i in range(n) if i != j] for j in range(count_vertex)}
    return graph


n = int(input('Введите число вершин графа: '))
print(gen_graph(n), sep='\n')
g = gen_graph(n)


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            dfs(graph, k, visited)
    return visited


s = int(input('Введите стартовую вершину графа: '))
print(dfs(g, s, visited=[]))