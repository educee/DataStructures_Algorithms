#Graph Representation in Matrix

#Given list of Vertices and edge list, represent this graph in a matrix representation

#Example:

#Graph 'G' with set of 'V' Vertices (vertex for single node), and 'E' pairs of Edges

# Vertices V = {a, d, m, n, f, g}
# Edges E = {[a,m], [m, g], [a, d], [f, n], [n, a]}

#  Edges in row, col will have 1 others 0(as there is no egde b/w them)

#    a  d  m  n  f  g
#  a 0  1  1  1  0  0
#  d 1  0  0  0  0  0
#  m 1  0  0  0  0  1
#  n 1  0  0  0  1  0
#  f 0  0  0  1  0  0
#  g 0  0  1  0  0  0



class Graph_adj_Matrix():
    
    def __init__(self, vertices=[None], edges = [None]): 
        self.vertices = [] if vertices is None else vertices
        
        self.edges = [] if edges is None else edges
        
        self.matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]
        
    def represent_graph_matrix(self):
        
        for rowIndex, element in enumerate(self.vertices):
            for columnIndex, ele in enumerate(self.vertices):
                if [element, ele] in self.edges or ([ele, element] in self.edges): #Try reducing time complexity here
                    self.matrix[rowIndex][columnIndex] = 1
                    
    def print_graph_matrix(self):
        #print(self.matrix)
        for row in range(len(self.vertices)):
            print('[', end=" ")
            for col in range(len(self.vertices)):
                print(self.matrix[row][col], end=" ")
            print(']\n')
            

if __name__ == "__main__":
    G = Graph_adj_Matrix(vertices=['a', 'd', 'm', 'n', 'f', 'g'], edges=[['a','m'], ['m', 'g'], ['a', 'd'], ['f', 'n'], ['n', 'a']])
    G.print_graph_matrix()
    G.represent_graph_matrix()
    G.print_graph_matrix()
