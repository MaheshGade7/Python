class Node:
    """Class representing a node in a linked list (used in adjacency list)."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    """Graph class using adjacency lists implemented via linked lists."""
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # Number of vertices in the graph
        # Create an adjacency list as a list of linked lists
        self.adj_list = [None] * num_vertices

    def add_edge(self, src, dest):
        """
        Add an edge from src to dest in the adjacency list.
        
        Args:
        src (int): Source vertex index
        dest (int): Destination vertex index
        """
        # Add dest to the linked list at index src
        new_node = Node(dest)
        new_node.next = self.adj_list[src]
        self.adj_list[src] = new_node

        # For undirected graphs, add src to the linked list at index dest
        new_node = Node(src)
        new_node.next = self.adj_list[dest]
        self.adj_list[dest] = new_node

    def display(self):
        """Display the adjacency matrix using linked lists."""
        print("\nAdjacency Matrix Representation (using linked lists):")
        for i in range(self.num_vertices):
            print(f"Vertex {i}:", end=" ")
            temp = self.adj_list[i]
            while temp:
                print(f"-> {temp.data}", end=" ")
                temp = temp.next
            print()


def main():
    """Main function to interact with the user and create a graph."""
    print("Graph implementation with adjacency lists (using linked lists).")
    
    # Input number of vertices
    num_vertices = int(input("Enter the number of vertices in the graph: "))
    graph = Graph(num_vertices)
    
    # Input number of edges
    num_edges = int(input("Enter the number of edges in the graph: "))

    # Input edges
    print("Enter the edges (source and destination pair):")
    for _ in range(num_edges):
        src, dest = map(int, input().split())
        graph.add_edge(src, dest)

    # Display adjacency lists as adjacency matrix
    graph.display()


if __name__ == "__main__":
    main()
