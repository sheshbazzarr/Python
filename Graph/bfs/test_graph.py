from graph import Graph
def print_graph(graph):
    print("Two dimenstional array output vertex edge and adjacent array ")

    length=len(graph.get_vertex())
    print(" ",end=" ")

    for i in range(0,length):
        print(graph.get_vertexs()[i].data,"",end="") 
    print()

    length=len(graph.get_adjacency_matrix())
    for i in range(0,length):
        print(graph.get_vertexs()[i].data,"",end="")
        for j in range(0,length):
            print(graph.get_adjacency_matrix()[i][j],"",end="")
        print()
def main():
    graph=Graph(5)

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")

    # add adjecany edges
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(0,3)
    graph.add_edge(0,4)
    graph.add_edge(1,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    graph.add_edge(2,3)
    graph.add_edge(2,4)
    graph.add_edge(3,4)

    print_graph(graph)
    print("\nbreadth-first search")
if __name__=="__main__":    
    main()
