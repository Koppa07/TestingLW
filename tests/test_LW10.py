import pytest

from src.string_io import StringReader, StringWriter
from src.LW10 import Graph

# Тесты для работы с заданным форматом файлов с использованием подмены

def test_read_edges():
    content = "1 2\n1 3\n2 4\n"
    reader = StringReader(content)
    result = reader.read()
    assert result == [
        (1,2),(1,3),(2,4)
    ]
def test_read_with_commentss_and_empty_lines():
    content ="""
    # Список ребер

    1 2
    1 3

    # Следующее ребро

    2 4
    """
    reader = StringReader(content)
    result = reader.read()
    assert result == [
        (1,2),(1,3),(2,4)
    ]

def test_read_empty_string():
    reader = StringReader("")
    result = reader.read()
    assert result==[]

def test_read_non_integer_vertices():
    content = "A B\n"
    reader = StringReader(content)
    with pytest.raises(ValueError):
        reader.read

def test_read_invalid_line():
    content = "1 2\n3\n"
    reader = StringReader(content)
    with pytest.raises(ValueError, match="Некорректная строка"):
        reader.read()

def test_write_adjacency_matrix():
    matrix = [[0,1,1],[1,0,0],[1,0,0]]
    writer = StringWriter()
    writer.write(None, matrix)
    result = writer.getValue()
    expected = ("0 1 1\n"
    "1 0 0\n"
    "1 0 0\n")
    assert result == expected

def test_write_empty_matrix():
    writer = StringWriter()
    writer.write(None, [])
    assert writer.getValue() == ""
    

# Тесты для графа с использованием заглушек и фиктивных объектов

class StubReader:
    # Заглушка для чтения списка рёбер.

    def __init__(self, edges):
        self.edges = edges

    def read(self, filename):
        return self.edges


class FakeWriter:
    # Фиктивный объект для сохранения матрицы в памяти.

    def __init__(self):
        self.filename = None
        self.matrix = None

    def write(self, filename, matrix):
        self.filename = filename
        self.matrix = [row[:] for row in matrix]

@pytest.fixture
def graph():
    edges = [
        (1, 2),
        (1, 3),
        (2, 4),
        (2, 5),
        (3, 6)
    ]

    reader = StubReader(edges)
    writer = FakeWriter()

    result = Graph(reader, writer)
    result.load_from_file("input.txt")

    return result

def test_load_from_edges(graph):
    assert graph.vertices == [1, 2, 3, 4, 5, 6]
    assert graph.n == 6


def test_adjacency_matrix(graph):
    expected = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0]
    ]

    assert graph.get_adjacency_matrix() == expected

test_data_dfs = [(1, [1, 2, 4, 5, 3, 6] ), (3, [3, 1, 2, 4, 5, 6])]

@pytest.mark.parametrize("start, expected", test_data_dfs)
def test_depth_first_search(graph, start, expected):
    result = graph.depth_first_search(start)

    assert result == expected

test_data_adjacent_vertices = [(2, [1,4,5]),(4,[2])]

@pytest.mark.parametrize("vertex, expected", test_data_adjacent_vertices)
def test_get_adjacent_vertices(graph, vertex, expected):
    result = graph.get_adjacent_vertices(vertex)

    assert result == expected


def test_invalid_vertex_dfs(graph):
    with pytest.raises(ValueError, match="отсутствует в графе"):
        graph.depth_first_search(100)


def test_invalid_vertex_adjacent(graph):
    with pytest.raises(ValueError, match="отсутствует в графе"):
        graph.get_adjacent_vertices(100)


def test_save_to_file(graph):
    """Проверка передачи матрицы фиктивному объекту записи."""

    graph.save_to_file("output.txt")

    assert graph.writer.filename == "output.txt"

    assert graph.writer.matrix == graph.get_adjacency_matrix()


def test_load_empty_graph():
    graph = Graph(StubReader([]), FakeWriter())
    graph.load_from_file("empty.txt")

    assert graph.vertices == set()
    assert graph.matrix == []
    assert graph.n == 0


def test_disconnected_graph():
    """Проверка DFS для несвязного графа."""

    graph = Graph(
        StubReader([(1, 2), (3, 4)]),
        FakeWriter()
    )
    graph.load_from_file("input.txt")

    assert graph.depth_first_search(1) == [1, 2]
    assert graph.depth_first_search(3) == [3, 4]


def test_reload_graph():
    """Проверка повторной загрузки другого графа."""

    graph = Graph(StubReader([]), FakeWriter())

    graph.load_from_edges([(1, 2), (2, 3)])
    graph.load_from_edges([(10, 20)])

    assert graph.vertices == [10, 20]
    assert graph.n == 2
    assert graph.get_adjacency_matrix() == [
        [0, 1],
        [1, 0]
    ]