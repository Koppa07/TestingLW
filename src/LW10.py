class Graph:
    def __init__(self, reader=None, writer=None):
        self.reader = reader
        self.writer = writer
        self.adjacency_matrix = []
        self.vertices = []

    def load_from_file(self, filename):
        edges = self.reader.read(filename)
        self.load_from_edges(edges)

    def save_to_file(self, filename):
        incidence_matrix = self.to_incidence_matrix()
        self.writer.write(filename, incidence_matrix)

    def load_from_edges(self, edges):
        if not edges:
            self.adjacency_matrix = []
            self.vertices = []
            return

        vertices = set()

        for start, end in edges:
            vertices.add(start)
            vertices.add(end)

        self.vertices = sorted(vertices)

        vertex_index = {vertex: index for index, vertex in enumerate(self.vertices)}

        size = len(self.vertices)

        self.adjacency_matrix = [[0 for _ in range(size)] for _ in range(size)]

        for start, end in edges:
            i = vertex_index[start]
            j = vertex_index[end]

            self.adjacency_matrix[i][j] = 1
            self.adjacency_matrix[j][i] = 1

    def get_adjacency_matrix(self):
        return self.adjacency_matrix

    def bfs(self, start_vertex=0):
        if not self.adjacency_matrix:
            return []

        if start_vertex < 0 or start_vertex >= len(self.adjacency_matrix):
            raise ValueError("Некорректный номер начальной вершины")

        visited = [False] * len(self.adjacency_matrix)
        queue = [start_vertex]
        result = []

        visited[start_vertex] = True

        while queue:
            vertex = queue.pop(0)
            result.append(vertex)

            for neighbour, connected in enumerate(self.adjacency_matrix[vertex]):
                if connected and not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

        return result

    def shortest_path(self, start, end):
        if not self.adjacency_matrix:
            return None

        if start not in self.vertices:
            raise ValueError("Начальная вершина отсутствует в графе")

        if end not in self.vertices:
            raise ValueError("Конечная вершина отсутствует в графе")

        start_index = self.vertices.index(start)
        end_index = self.vertices.index(end)

        size = len(self.vertices)

        queue = [start_index]

        visited = [False] * size
        previous = [None] * size

        visited[start_index] = True

        while queue:
            current = queue.pop(0)

            if current == end_index:
                break

            for neighbour, connected in enumerate(self.adjacency_matrix[current]):
                if connected and not visited[neighbour]:
                    visited[neighbour] = True
                    previous[neighbour] = current
                    queue.append(neighbour)

        if not visited[end_index]:
            return None

        path = []
        current = end_index

        while current is not None:
            path.append(self.vertices[current])
            current = previous[current]

        path.reverse()

        return path

    def to_incidence_matrix(self):
        if not self.adjacency_matrix:
            return []

        edges = []
        size = len(self.adjacency_matrix)

        for i in range(size):
            for j in range(i + 1, size):
                if self.adjacency_matrix[i][j] == 1:
                    edges.append((i, j))

        incidence_matrix = [[0 for _ in range(len(edges))] for _ in range(size)]

        for edge_index, (start, end) in enumerate(edges):
            incidence_matrix[start][edge_index] = 1
            incidence_matrix[end][edge_index] = 1

        return incidence_matrix


class GraphReader:
    def read(self, filename):
        edges = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                start, end = map(int, line.split())
                edges.append((start, end))

        return edges


class GraphWriter:
    def write(self, filename, matrix):
        with open(filename, "w", encoding="utf-8") as file:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")
