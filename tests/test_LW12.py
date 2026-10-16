import pytest
from unittest.mock import Mock
from assertpy import assert_that
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
    assert_that(graph.vertices).contains(1,2,3,4,5,6)
    assert_that(graph.n).is_equal_to(6)

def test_adjacency_matrix(graph):
    matrix = graph.get_adjacency_matrix()
    excepted = [[0,1,1,0,0,0],[1,0,0,1,1,0],[1,0,0,0,0,1],[0,1,0,0,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0]]
    assert_that(matrix).is_equal_to(excepted)

def test_dfs(graph):
    result = graph.depth_first_search(1)
    assert_that(result).is_equal_to([1,2,4,5,3,6])

def test_get_adjacent_vertices(graph):
    result =graph.get_adjacent_vertices(2)
    assert_that(result).contains(1,4,5)
    assert_that(result).does_not_contain(2,3,6)

def test_empty_graph():
    graph = Graph()
    graph.load_from_edges([])
    assert_that(graph.vertices).is_empty()
    assert_that(graph.matrix).is_empty()
    assert_that(graph.n).is_zero()
    assert_that(graph.vertex_to_index).is_empty()

def test_disconnected_graph():
    graph = Graph()
    graph.load_from_edges([1,2],[3,4])
    first_component = graph.depth_first_search(1)
    second_component = graph.depth_first_search(3)
    assert_that(first_component).contains(1,2)
    assert_that(first_component).is_length(2)
    assert_that(second_component).contains(3,4)
    assert_that(second_component).is_length(2)
    assert_that(first_component).does_not_contain(3,4)
    assert_that(second_component).does_not_contain(1,2)

def test_single_edge():
    graph = Graph()
    graph.load_from_edges([(10,20)])
    assert_that(graph.vertices).contains(10,20)
    assert_that(graph.n).is_equal_to(2)
    assert_that(graph.get_adjacency_matrix()).is_equal_to([[0,1],[1,0]])

def test_save_to_file(graph):
    graph.save_to_file("output.txt")
    graph.writer.write.assert_called_once_with()
    args = graph.writer.write.write.call_args.args
    assert_that(args[0]).is_equal_to("output.txt")