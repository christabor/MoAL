# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

# See mathworld.wolfram.com/AdjacencyMatrix.html for a nice explanation.


class GraphMatrix(object):

    def __init__(self):
        """
        The matrix structure is just a list of lists,
        where each sublist represents a row. A separate nodes dictionary
        is used for fast lookups to reference which row/column to look at
        when doing operations.
            e.g.
            >>> nodes = {'A': 0, 'B': 1, ... },
            >>> matrix = [[0, 1], [1, 0], ...]
        """
        self.vertices, self.edges, self.matrix = {}, {}, []
        self.vertex_count, self.edge_count = 0, 0

    def __setitem__(self, new_vertex, connections):
        """Adds a new vertex, and adds any connections that may not exist."""
        if new_vertex not in self.vertices:
            # Defer to helper for non-edge cases
            self._add(new_vertex)
        # Update the actual values with connections
        for connection in connections:
            # Add this new vertex if it's not in the set already.
            if connection not in self.vertices:
                self._add(connection)
            # Add edge connections.
            self._add_edge(new_vertex, connection)

    def __delitem__(self, vertex):
        """Deletes a vertex and flips all adjacent connections to off."""
        # Store a reference to the row/col before deleting
        if vertex not in self.vertices:
            return
        row = self.vertices[vertex]
        col = row
        del self.vertices[vertex]
        # Delete entire row.
        del self.matrix[row]
        # Reorder is only necessary for deletions.
        self._reorder_vertices()
        # Decrement current count
        self.vertex_count -= 1
        # Remove the matching column for each row
        for row_list in self.matrix:
            row_list.pop(col)

    def __str__(self):
        """Visualize the matrix as a table"""
        # Top row - just print the keys + space
        print('  ' + ' '.join(self.vertices.keys()))
        # Subsequent rows - get label for first col, then the remainder cols
        for label, index in self.vertices.iteritems():
            print('{} {}'.format(label, self.matrix[index]))
        return ''

    def _zeros(self, count):
        return [0 for n in range(count)]

    def _new_row(self, count):
        self.matrix.append(self._zeros(count))

    def degree(self, vertex):
        """Another interesting feature of Adjacency matrices is the
        fact that any row or column summed is automatically
        the degree of that vertex -- magical!"""
        if vertex not in self.vertices:
            return 0
        row = self.vertices[vertex]
        return sum(self.matrix[row])

    def has_edge(self, start, end):
        if start not in self.vertices or end not in self.vertices:
            return False
        # Start, end corresponds to row, col
        row, col = self.vertices[start], self.vertices[end]
        return self.matrix[row][col] == 1

    def get_row_vals(self, label):
        """Returns the range slice of a given label, representing the row."""
        row = self.vertices[label]
        return self.matrix[row]

    def _fill_previous_rows(self, count):
        """Fill previous rows to ensure the row length is always equal."""
        for index, row in enumerate(self.matrix):
            row_len = len(row)
            # If there is any discrepancy in length, update the rows.
            if row_len < count:
                offset = count - row_len
                # Fill with zeros
                self.matrix[index] += self._zeros(offset)

    def _add(self, new_vertex):
        # Set the new vertex value to the **current** count
        self.vertices[new_vertex] = self.vertex_count
        # Add new row, filled with zeros.
        self._new_row(self.vertex_count)
        # Increment, before filling is done, but after setting of new vertex.
        self.vertex_count += 1
        # Since matrix has expanded,
        # fill in the missing columns in previous rows
        self._fill_previous_rows(self.vertex_count)

    def _reorder_vertices(self):
        """Using a dictionary for the label lookup makes setting/getting items
        very fast, but the downside is that the indices must be re-ordered
        if any items are deleted. The flip-side then, would be to use a list
        -- but lookups would suffer the same problem -- so, the problem is
        reversed. It could however, be tuned to work either way,
        depending on access patterns, but that is well beyond the scope here.
        """
        self.vertices = self._reorder_dict_indices(self.vertices)

    def _reorder_edges(self):
        self._reorder_dict_indices(self.edges)

    def _reorder_dict_indices(self, vals):
        """Generic reordering function for resetting
        indices of a given dictionary."""
        for new_index, index in enumerate(vals):
            vals[index] = new_index
        return vals

    def _remove_edge(self, start, end):
        """Removes an edge"""
        row, col = self.vertices[start], self.vertices[end]
        self.matrix[row][col] = 0

    def _add_edge(self, start, end):
        """Adds an edge"""
        row, col = self.vertices[start], self.vertices[end]
        self.matrix[row][col] = 1

    def get_column_vals(self, label):
        """Returns a list of values representing the given
        labels column values."""
        col = self.vertices[label]
        return [row[col] for row in self.matrix]


class AdjacencyMatrix(GraphMatrix):
    """
    [Wikipedia]
    "In mathematics and computer science, an adjacency matrix
    is a means of representing which vertices of a graph are
    adjacent to which other vertices."

    ...In other words, it's another way to represent a graph, very compactly
    (and thus efficiently), by using a matrix that represents the connections
    -- by mapping the row and column to a specific node (similar technique
    as a Cayley or multiplication table).

       A  B  C  D
    A  0  1  1  0     might correspond to:
    B  1  0  1  1     (row A, col A) = 0,
    C  1  1  0  0     (row B, col A) = 1, etc...
    D  1  0  0  0     generally, self referencing nodes are not
                      represented, but if they are, their value is 2.
    """


if __name__ == '__main__':
    with Section('Adjacency Matrix'):
        amatrix = AdjacencyMatrix()
        amatrix['A'] = ['B']
        amatrix['B'] = ['A']
        print(amatrix)

        amatrix['B'] = ['A', 'C']
        amatrix['C'] = ['B', 'A']
        print(amatrix)

        amatrix['D'] = ['C', 'B', 'A']
        print(amatrix)

        amatrix['E'] = ['D', 'C', 'B', 'A']
        amatrix['F'] = ['A', 'B', 'C', 'D', 'E']
        amatrix['E'] = ['A', 'B', 'C', 'D', 'F']  # Add more connections
        amatrix['A'] = ['F']  # Add incoming connection for F
        print(amatrix)

        assert amatrix.has_edge('B', 'C')  # True
        assert not amatrix.has_edge('B', 'B')  # False

        assert amatrix.vertices == {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
        assert amatrix.degree('A') == 2  # True (B, F)
        assert amatrix.degree('C') == 2  # True (B, A)
        assert amatrix.degree('F') == 5  # True (A, B, C, D, E)

        del amatrix['A']
        del amatrix['B']
        print(amatrix)

        assert amatrix.vertices == {
            'C': 0, 'E': 1, 'D': 2, 'F': 3}
        assert not amatrix.has_edge('B', 'C')  # False, deleted
        assert amatrix.degree('B') == 0  # True, deleted
        assert amatrix.degree('A') == 0  # True
        assert amatrix.degree('C') == 0  # True, B, C deleted
