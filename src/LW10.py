class Graph:
    def __init__(self, reader=None, writer=None):
        self.reader = reader
        self.writer = writer
        self.vertices = set()
        self.matrix = []
        self.vertex_to_index = dict()
        self.n = 0

    def load_from_file(self, filename):
        edges = self.reader.read(filename)
        self.load_from_edges(edges)

    def load_from_edges(self, edges):
        self.vertices = set()
        self.matrix = []
        self.n = 0
        self.vertex_to_index = {}
        
        if not edges:
            self.matrix = []
            self.vertices = set()
            return

        for u, v in edges:
            self.vertices.add(u)
            self.vertices.add(v)

        self.vertices = sorted(self.vertices)

        self.vertex_to_index = {vertex: index for index, vertex in enumerate(self.vertices)}

        self.n = len(self.vertices)

        self.matrix = [[0]*self.n for _ in range(self.n)]

        for u, v in edges:
            i = self.vertex_to_index[u]
            j = self.vertex_to_index[v]

            self.matrix[i][j] = 1
            self.matrix[j][i] = 1

    def save_to_file(self,filename):
        matrix = self.get_adjacency_matrix()
        self.writer.write(filename, matrix)

    def get_adjacency_matrix(self):
        return self.matrix

    def depth_first_search(self, start):
        if start not in self.vertex_to_index:
            raise ValueError(f"Вершина {start} отсутствует в графе")

        visited = set()
        result = []

        def dfs(vertex):
            visited.add(vertex)
            result.append(vertex)

            index = self.vertex_to_index[vertex]

            for j in range(self.n):
                if self.matrix[index][j] == 1:
                    neighbor = self.vertices[j]
                    if neighbor not in visited:
                        dfs(neighbor)

        dfs(start)
        
        return result

    def get_adjacent_vertices(self, vertex):
        if vertex not in self.vertex_to_index:
            raise ValueError(f"Вершина {vertex} отсутствует в графе")

        adjacent = []
        index = self.vertex_to_index[vertex]

        for j in range(self.n):
            if self.matrix[index][j] ==1:
                adjacent.append(self.vertices[j])

        return adjacent

    def print_matrix(self):
        print("Матрица смежности:")

        print("   ", *self.vertices)

        for i, row in enumerate(self.matrix):
            print(self.vertices[i], row)



class GraphReader:
    def read(self, filename):
        edges = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = line.split()

                if len(parts) != 2:
                    raise ValueError(f"Некорректная строка в файле: {line}")

                u,v = map(int, parts)
                edges.append((u,v))

        return edges


class GraphWriter:
    def write(self, filename, matrix):
        with open(filename, "w", encoding="utf-8") as file:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")