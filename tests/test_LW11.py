import pytest
from unittest.mock import Mock
from src.LW10 import Graph, GraphReader, GraphWriter

@pytest.fixture
def graph():
    edges = [(1,2),(1,3),(2,4),(2,5),(3,6)]
    reader = Mock(spec=GraphReader)
    writer = Mock(spec=GraphWriter)
    reader.read.return_value = edges
    graph = Graph(reader, writer)
    graph.load_from_file("input.txt")
    return graph

def test_load_from_file(graph):
    graph.reader.read.assert_called_once_with("input.txt")
    assert graph.vertices == [1,2,3,4,5,6]

def test_adjacency_matrix(graph):
    excepted = [[0,1,1,0,0,0],[1,0,0,1,1,0],[1,0,0,0,0,1],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]]
    assert graph.get_adjacency_matrix() == excepted

def test_dfs(graph):
    result = graph.depth_first_search(1)
    assert result == [1,2,4,5,3,6]

def test_get_adjacent_vertices(graph):
    result =graph.get_adjacent_vertices(2)
    assert result == [1,4,5]

def test_dfs_invalid_vertex(graph):
    with pytest.raises(ValueError, match="отсутствует в графе"):
        graph.depth_first_search(100)
def test_adjancet_invalid_vertex(graph):
    with pytest.raises(ValueError, match="отсутствует в графе"):
            graph.get_adjacent_vertices(100)

def test_save_to_file(graph):
    expected = graph.get_adjacency_matrix()
    graph.save_to_file("output.txt")
    graph.writer.write.assert_called_once_with("output.txt", expected)

def test_reader_not_called(graph):
    graph.reader.reset_mock()
    graph.depth_first_search(1)
    graph.reader.read.assert_not_called()

def test_writer_not_called(graph):
    graph.writer.reset_mock()
    graph.depth_first_search(1)
    graph.writer.write.assert_not_called()

def test_empty_graph():
    reader = Mock()
    writer = Mock()
    reader.read.return_value = []
    graph = Graph(reader, writer)
    graph.load_from_file("empty.txt")
    assert graph.vertices == []
    assert graph.matrix == []
    assert graph.n == 0

def test_disconnected_graph():
    reader = Mock()
    writer = Mock()
    reader.read.return_value = [(1,2),(3,4)]
    graph = Graph(reader, writer)
    graph.load_from_file("input.txt")
    assert graph.depth_first_search(1) == [1,2]
    assert graph.depth_first_search(3) == [3,4]