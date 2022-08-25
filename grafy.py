# class Wezel:
#     def __init__(self, wartosc, sasiad1, sasiad2, sasiad3):
#         self.wartosc = wartosc
#         self.sasiad1 = sasiad1
#         self.sasiad2 = sasiad2
#         self.sasiad3 = sasiad3


graph = {"A":["B","C"], "B":["C","D"], "C":["D"], "D":["C"], "E":["C"], "F":[]}

def add_node(graph, node):
    """Wstawia wierzchołek do grafu."""
    if node not in graph:
        graph[node] = []


